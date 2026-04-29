#!/usr/bin/env python3
"""
Generate the GitHub Pages dashboard for the Mailchimp Growth Strategist.

Reads:
  analyses/<YYYY-WW>/00-executive-brief.md
  analyses/<YYYY-WW>/01-08-*.md
  analyses/<YYYY-WW>/_prediction_grading.json
  predictions-ledger.jsonl
  findings-ledger.jsonl

Writes:
  dashboards/index.html

Reuses the pattern from last-stretch-voc-analyzer (Jinja2 + static HTML).

Usage:
  python3 scripts/generate_dashboard.py [YYYY-WW]
  (defaults to current ISO week)
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Optional Jinja2 dependency. If missing, fall back to plain string formatting
# so the dashboard still generates in degraded mode (helpful in CI/local envs
# without `pip install jinja2`).
try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    JINJA_AVAILABLE = True
except ImportError:
    JINJA_AVAILABLE = False


def current_iso_week() -> str:
    now = datetime.now(timezone.utc)
    year, week, _ = now.isocalendar()
    return f"{year}-W{week:02d}"


def load_brief(week_dir: Path) -> str:
    p = week_dir / "00-executive-brief.md"
    return p.read_text() if p.exists() else "# Brief not yet generated\n"


def load_analyses(week_dir: Path) -> list[tuple[str, str]]:
    out = []
    for p in sorted(week_dir.glob("0[1-8]-*.md")):
        out.append((p.stem, p.read_text()))
    return out


def load_predictions(predictions_path: Path) -> dict:
    if not predictions_path.exists():
        return {"open": [], "graded": [], "rolling_hit_rate": None}

    open_preds = []
    graded_preds = []
    grade_index = {}

    with predictions_path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue

            if "grade_for_recommendation_id" in row:
                grade_index[row["grade_for_recommendation_id"]] = row
            elif "recommendation_id" in row:
                if row.get("actual_delta") is not None:
                    graded_preds.append(row)
                else:
                    open_preds.append(row)

    # Match grades back to predictions
    for pred in list(open_preds):
        if pred["recommendation_id"] in grade_index:
            graded_preds.append({**pred, **grade_index[pred["recommendation_id"]]})
            open_preds.remove(pred)

    # Compute rolling 12-week hit rate
    cutoff = datetime.now(timezone.utc).timestamp() - 12 * 7 * 86400
    recent = []
    for g in graded_preds:
        ga = g.get("graded_at")
        if not ga:
            continue
        try:
            ts = datetime.fromisoformat(ga.replace("Z", "+00:00")).timestamp()
        except ValueError:
            continue
        if ts >= cutoff and g.get("hit_classification") in ("hit", "miss"):
            recent.append(g)

    if recent:
        hits = sum(1 for r in recent if r["hit_classification"] == "hit")
        hit_rate = hits / len(recent)
    else:
        hit_rate = None

    return {
        "open": open_preds,
        "graded": graded_preds,
        "rolling_hit_rate": hit_rate,
        "n_graded_12w": len(recent),
    }


def render_html(week_id: str, brief_md: str, analyses: list, predictions: dict) -> str:
    title = f"Mailchimp Growth Strategist — {week_id}"

    if JINJA_AVAILABLE:
        env = Environment(
            loader=FileSystemLoader(str(REPO_ROOT / "dashboards" / "templates")),
            autoescape=select_autoescape(["html"]),
        )
        try:
            tmpl = env.get_template("index.html.j2")
            return tmpl.render(
                title=title,
                week_id=week_id,
                generated_at=datetime.now(timezone.utc).isoformat(),
                brief_md=brief_md,
                analyses=analyses,
                predictions=predictions,
            )
        except Exception:
            pass

    # Fallback: minimal inline HTML
    parts = [
        f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title>",
        "<style>body{font-family:system-ui,-apple-system,sans-serif;max-width:1080px;margin:32px auto;padding:0 16px;color:#1f2937}",
        "h1,h2,h3{color:#111827} pre{background:#f3f4f6;padding:12px;border-radius:6px;overflow-x:auto}",
        "code{background:#f3f4f6;padding:2px 6px;border-radius:4px}",
        "table{border-collapse:collapse;width:100%;margin:12px 0} th,td{border:1px solid #e5e7eb;padding:6px 10px;text-align:left}",
        "details{margin:16px 0;border:1px solid #e5e7eb;border-radius:8px;padding:12px}",
        "summary{cursor:pointer;font-weight:600;color:#0d6efd}",
        ".banner{background:#fef3c7;border-left:4px solid #f59e0b;padding:10px 14px;margin:14px 0;border-radius:6px}",
        ".hit-rate{display:inline-block;font-size:1.2em;font-weight:700;padding:6px 12px;border-radius:6px}",
        ".hit-rate.high{background:#d1fae5;color:#065f46}",
        ".hit-rate.med{background:#fef3c7;color:#92400e}",
        ".hit-rate.low{background:#fee2e2;color:#991b1b}",
        "</style></head><body>",
        f"<h1>{title}</h1>",
        f"<p><em>Generated: {datetime.now(timezone.utc).isoformat()}</em></p>",
    ]

    rate = predictions.get("rolling_hit_rate")
    n_graded = predictions.get("n_graded_12w", 0)
    if rate is None:
        parts.append(f"<p class='banner'>No graded predictions in last 12 weeks ({n_graded} graded).</p>")
    else:
        cls = "high" if rate >= 0.6 else ("med" if rate >= 0.4 else "low")
        parts.append(f"<p>Rolling 12-week prediction hit rate: <span class='hit-rate {cls}'>{rate:.0%}</span> (n={n_graded})</p>")

    parts.append("<h2>Executive Brief</h2><pre>" + escape(brief_md) + "</pre>")

    if analyses:
        parts.append("<h2>Supporting Analyses</h2>")
        for stem, content in analyses:
            parts.append(f"<details><summary>{escape(stem)}</summary><pre>{escape(content)}</pre></details>")

    parts.append(f"<h2>Open Predictions ({len(predictions.get('open', []))})</h2>")
    if predictions.get("open"):
        parts.append("<table><tr><th>Recommendation</th><th>Predicted metric</th><th>Predicted delta</th><th>Window days</th><th>Due</th></tr>")
        for p in predictions["open"]:
            parts.append(
                "<tr>"
                f"<td>{escape(p.get('title', p.get('recommendation_id', '?')))}</td>"
                f"<td>{escape(p.get('predicted_metric', ''))}</td>"
                f"<td>{escape(str(p.get('predicted_delta', '')))}</td>"
                f"<td>{escape(str(p.get('predicted_window_days', '')))}</td>"
                f"<td>{escape(p.get('predicted_due_at', ''))}</td>"
                "</tr>"
            )
        parts.append("</table>")
    else:
        parts.append("<p><em>No open predictions.</em></p>")

    parts.append("</body></html>")
    return "\n".join(parts)


def escape(s: str) -> str:
    if not s:
        return ""
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def main() -> int:
    week_id = sys.argv[1] if len(sys.argv) > 1 else current_iso_week()
    week_dir = REPO_ROOT / "analyses" / week_id

    if not week_dir.exists():
        print(f"WARN: {week_dir} does not exist; generating empty dashboard for {week_id}", file=sys.stderr)
        week_dir.mkdir(parents=True, exist_ok=True)

    brief_md = load_brief(week_dir)
    analyses = load_analyses(week_dir)
    predictions = load_predictions(REPO_ROOT / "predictions-ledger.jsonl")

    html = render_html(week_id, brief_md, analyses, predictions)

    out_path = REPO_ROOT / "dashboards" / "index.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html)

    # Also write a per-week archive
    archive = REPO_ROOT / "dashboards" / "archive" / f"{week_id}.html"
    archive.parent.mkdir(parents=True, exist_ok=True)
    archive.write_text(html)

    print(f"Dashboard written to {out_path}")
    print(f"Archive written to {archive}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
