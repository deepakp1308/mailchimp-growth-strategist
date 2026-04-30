#!/usr/bin/env python3
"""
Generate the GitHub Pages dashboard for the Mailchimp Growth Strategist.

Renders a consulting-style report from analyses/<YYYY-WW>/ with:
- Sidebar navigation
- Top-3 recommendation cards (color-coded by verdict)
- Falsifiable-prediction tracker (rolling 12-week hit rate)
- 8 supporting analyses (rendered markdown, collapsible)
- Contradictions ledger panel
- Strategy-vs-execution scorecard

Reuses the pattern from last-stretch-voc-analyzer (markdown -> single static HTML).

Usage:
  python3 scripts/generate_dashboard.py [YYYY-WW]
  (defaults to current ISO week)

Outputs:
  dashboards/index.html           (single-page report — current week as headline)
  dashboards/archive/YYYY-WW.html (per-week archive)
  dashboards/_data/<YYYY-WW>.json (raw structured data for downstream use)
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

try:
    import markdown
    MD_AVAILABLE = True
except ImportError:
    MD_AVAILABLE = False


def render_md(md_text: str) -> str:
    """Render markdown to HTML, with graceful fallback."""
    if not MD_AVAILABLE:
        return f"<pre>{escape(md_text)}</pre>"
    return markdown.markdown(
        md_text,
        extensions=["extra", "tables", "fenced_code", "sane_lists", "toc"],
        output_format="html5",
    )


def escape(s: str) -> str:
    if not s:
        return ""
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def current_iso_week() -> str:
    now = datetime.now(timezone.utc)
    year, week, _ = now.isocalendar()
    return f"{year}-W{week:02d}"


def list_archive_weeks(analyses_dir: Path) -> list[str]:
    if not analyses_dir.exists():
        return []
    weeks = sorted(
        [
            p.name
            for p in analyses_dir.iterdir()
            if p.is_dir() and re.match(r"^\d{4}-W\d{2}$", p.name)
        ],
        reverse=True,
    )
    return weeks


def load_brief(week_dir: Path) -> str:
    p = week_dir / "00-executive-brief.md"
    return p.read_text() if p.exists() else "# Brief not yet generated\n"


def load_analyses(week_dir: Path) -> list[tuple[str, str, str]]:
    """Return list of (slug, title, html_content).
    Glob catches 01-99 numbered analysis files; the executive brief (00-*) is rendered separately.
    """
    out = []
    for p in sorted(week_dir.glob("[0-9][1-9]-*.md")):
        if p.stem.startswith("00-"):
            continue
        text = p.read_text()
        # Title from first # heading or filename
        m = re.search(r"^# (.+)$", text, re.MULTILINE)
        title = m.group(1).strip() if m else p.stem
        out.append((p.stem, title, render_md(text)))
    return out


def load_predictions(predictions_path: Path) -> dict:
    if not predictions_path.exists():
        return {"open": [], "graded": [], "rolling_hit_rate": None, "n_graded_12w": 0}

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


def parse_recommendations(brief_md: str) -> list[dict]:
    """Pull the top-3 recommendations from the executive brief markdown."""
    recs = []
    pattern = re.compile(
        r"### #(\d+) — (.+?) — \*\*(.+?)\*\*\s*\n\n(.*?)(?=^###\s|^##\s|\Z)",
        re.DOTALL | re.MULTILINE,
    )
    for m in pattern.finditer(brief_md):
        num = m.group(1)
        title = m.group(2).strip()
        verdict = m.group(3).strip()
        body = m.group(4).strip()

        verdict_class = "verdict-info"
        v_low = verdict.lower()
        if "commit" in v_low and "conditional" not in v_low:
            verdict_class = "verdict-commit"
        elif "conditional" in v_low:
            verdict_class = "verdict-conditional"
        elif "pol" in v_low or "probe" in v_low:
            verdict_class = "verdict-probe"
        elif "no-commit" in v_low or "no commit" in v_low:
            verdict_class = "verdict-no"

        # Pull the predicted-metric block if present
        pred_match = re.search(
            r"\*\*Predicted metric movement.*?\*\*\s*\n((?:.*\n)+?)(?:\n##|\n-\s\*\*Confidence|\Z)",
            body,
        )
        pred_block = pred_match.group(1).strip() if pred_match else ""

        recs.append(
            {
                "num": num,
                "title": title,
                "verdict": verdict,
                "verdict_class": verdict_class,
                "body_html": render_md(body),
                "pred_html": render_md(pred_block) if pred_block else "",
            }
        )
    return recs


def parse_scqa(brief_md: str) -> dict:
    out = {"situation": "", "complication": "", "question": "", "answer": ""}
    for key in out.keys():
        m = re.search(
            rf"\*\*{key.capitalize()}:\*\*\s*(.+?)(?=\n-\s\*\*|\Z)",
            brief_md,
            re.DOTALL,
        )
        if m:
            out[key] = m.group(1).strip()
    return out


def load_contradictions(contradictions_path: Path) -> str:
    if not contradictions_path.exists():
        return ""
    return contradictions_path.read_text()


def load_findings_summary(findings_path: Path, week_id: str) -> list[dict]:
    """Pull findings-ledger rows from this week's run."""
    if not findings_path.exists():
        return []
    out = []
    with findings_path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            cit = " ".join(row.get("citations", []))
            if week_id in cit or week_id in row.get("ts", ""):
                out.append(row)
    return out


CSS = """
:root {
  --bg: #ffffff;
  --fg: #1f2937;
  --muted: #6b7280;
  --line: #e5e7eb;
  --accent: #2563eb;
  --green: #059669;
  --green-bg: #d1fae5;
  --amber: #d97706;
  --amber-bg: #fef3c7;
  --red: #dc2626;
  --red-bg: #fee2e2;
  --blue-bg: #dbeafe;
  --gray-bg: #f3f4f6;
}
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  font-size: 15px;
  line-height: 1.55;
  color: var(--fg);
  background: var(--bg);
  margin: 0;
  padding: 0;
}
.layout { display: grid; grid-template-columns: 260px 1fr; min-height: 100vh; }
nav.sidebar {
  background: #f9fafb;
  border-right: 1px solid var(--line);
  padding: 24px 18px;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
}
nav.sidebar h2 { font-size: 13px; text-transform: uppercase; letter-spacing: .05em; color: var(--muted); margin: 24px 0 8px; }
nav.sidebar h2:first-child { margin-top: 0; }
nav.sidebar ul { list-style: none; padding: 0; margin: 0 0 12px 0; }
nav.sidebar li { margin: 4px 0; }
nav.sidebar a { color: var(--fg); text-decoration: none; font-size: 14px; display: block; padding: 4px 8px; border-radius: 4px; }
nav.sidebar a:hover { background: var(--blue-bg); color: var(--accent); }
nav.sidebar .week-nav { font-size: 12px; }
main { padding: 36px 56px 80px; max-width: 1100px; }
.title-block h1 { margin: 0 0 6px; font-size: 30px; }
.title-block .subtitle { color: var(--muted); font-size: 14px; }
.hit-rate-card {
  display: inline-flex; gap: 16px; align-items: center;
  background: var(--gray-bg); padding: 12px 18px; border-radius: 8px;
  margin: 18px 0 28px; border: 1px solid var(--line);
}
.hit-rate-pill { display: inline-block; padding: 4px 10px; border-radius: 4px; font-weight: 700; font-size: 13px; }
.hit-rate-pill.high { background: var(--green-bg); color: var(--green); }
.hit-rate-pill.med { background: var(--amber-bg); color: var(--amber); }
.hit-rate-pill.low { background: var(--red-bg); color: var(--red); }
.hit-rate-pill.none { background: var(--gray-bg); color: var(--muted); }

.scqa { background: linear-gradient(180deg, #f0f9ff 0%, #ffffff 100%); border-left: 4px solid var(--accent); padding: 18px 22px; border-radius: 6px; margin: 20px 0 32px; }
.scqa h2 { margin-top: 0; font-size: 14px; text-transform: uppercase; letter-spacing: .05em; color: var(--accent); }
.scqa dl { margin: 0; }
.scqa dt { font-weight: 700; margin-top: 10px; color: var(--fg); }
.scqa dt:first-child { margin-top: 0; }
.scqa dd { margin: 4px 0 0; padding: 0; color: var(--fg); }
.scqa dd p { margin: 0; }

section.recs { margin: 32px 0; }
section.recs h2 { margin: 0 0 18px; font-size: 22px; }
.rec-grid { display: grid; gap: 18px; }
.rec-card { border: 1px solid var(--line); border-radius: 10px; padding: 22px 26px; background: white; box-shadow: 0 1px 3px rgba(0,0,0,0.03); }
.rec-card h3 { margin: 0 0 8px; font-size: 18px; display: flex; align-items: center; gap: 12px; }
.rec-card .num { display: inline-block; width: 28px; height: 28px; line-height: 28px; text-align: center; background: var(--gray-bg); border-radius: 50%; font-weight: 700; font-size: 14px; }
.rec-card .verdict { display: inline-block; padding: 3px 10px; border-radius: 4px; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: .03em; }
.rec-card .verdict.verdict-commit { background: var(--green-bg); color: var(--green); }
.rec-card .verdict.verdict-conditional { background: var(--amber-bg); color: var(--amber); }
.rec-card .verdict.verdict-probe { background: var(--blue-bg); color: var(--accent); }
.rec-card .verdict.verdict-no { background: var(--red-bg); color: var(--red); }
.rec-card .pred-callout { margin-top: 14px; padding: 12px 16px; background: var(--gray-bg); border-radius: 6px; border-left: 3px solid var(--accent); font-size: 14px; }
.rec-card .pred-callout strong { color: var(--accent); }
.rec-card details > summary { cursor: pointer; color: var(--accent); font-weight: 600; margin-top: 14px; padding: 6px 0; user-select: none; }
.rec-card details[open] > summary { margin-bottom: 8px; }
.rec-card details .body-html { padding: 6px 0 0; }

section.predictions, section.contradictions, section.analyses { margin: 36px 0; }
section h2 { margin: 0 0 14px; font-size: 22px; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 14px; }
th, td { border: 1px solid var(--line); padding: 8px 12px; text-align: left; vertical-align: top; }
th { background: var(--gray-bg); font-weight: 600; font-size: 13px; text-transform: uppercase; letter-spacing: .03em; color: var(--muted); }
tr:nth-child(2n) td { background: #fafafa; }

details.analysis-card { border: 1px solid var(--line); border-radius: 8px; padding: 16px 20px; margin: 12px 0; background: white; }
details.analysis-card > summary { cursor: pointer; font-weight: 600; font-size: 16px; color: var(--fg); padding: 4px 0; }
details.analysis-card[open] > summary { border-bottom: 1px solid var(--line); padding-bottom: 10px; margin-bottom: 12px; }

pre { background: var(--gray-bg); padding: 12px 16px; border-radius: 6px; overflow-x: auto; font-size: 13px; line-height: 1.4; }
code { background: var(--gray-bg); padding: 2px 6px; border-radius: 3px; font-size: 13px; font-family: ui-monospace, "SF Mono", Menlo, monospace; }
pre code { padding: 0; background: transparent; font-size: inherit; }
blockquote { margin: 16px 0; padding: 8px 16px; border-left: 3px solid var(--line); color: var(--muted); }

.banner { padding: 12px 16px; border-radius: 6px; margin: 16px 0; }
.banner.info { background: var(--blue-bg); border-left: 4px solid var(--accent); color: var(--accent); }
.banner.warn { background: var(--amber-bg); border-left: 4px solid var(--amber); color: var(--amber); }

.footer { margin-top: 48px; padding-top: 18px; border-top: 1px solid var(--line); color: var(--muted); font-size: 13px; }
.footer a { color: var(--accent); }

@media (max-width: 800px) {
  .layout { grid-template-columns: 1fr; }
  nav.sidebar { position: static; height: auto; border-right: none; border-bottom: 1px solid var(--line); }
  main { padding: 24px; }
}
"""


def build_html(week_id: str, week_dir: Path, all_weeks: list[str]) -> str:
    brief_md = load_brief(week_dir)
    analyses = load_analyses(week_dir)
    predictions = load_predictions(REPO_ROOT / "predictions-ledger.jsonl")
    contradictions_md = load_contradictions(REPO_ROOT / "contradictions.md")
    findings = load_findings_summary(REPO_ROOT / "findings-ledger.jsonl", week_id)

    recs = parse_recommendations(brief_md)
    scqa = parse_scqa(brief_md)

    # Hit-rate badge
    rate = predictions.get("rolling_hit_rate")
    n_graded = predictions.get("n_graded_12w", 0)
    if rate is None:
        rate_html = (
            f'<span class="hit-rate-pill none">no data</span> '
            f'<span style="color:var(--muted)">{n_graded} graded predictions in last 12 weeks</span>'
        )
    else:
        cls = "high" if rate >= 0.6 else ("med" if rate >= 0.4 else "low")
        rate_html = (
            f'<span class="hit-rate-pill {cls}">{rate:.0%}</span> '
            f'<span style="color:var(--muted)">{n_graded} graded predictions, last 12 weeks</span>'
        )

    # SCQA
    scqa_html = "<dl>"
    for key, label in [
        ("situation", "Situation"),
        ("complication", "Complication"),
        ("question", "Question"),
        ("answer", "Answer"),
    ]:
        if scqa.get(key):
            scqa_html += f"<dt>{label}</dt><dd>{render_md(scqa[key])}</dd>"
    scqa_html += "</dl>"

    # Recommendations
    if recs:
        rec_html = '<div class="rec-grid">'
        for r in recs:
            pred_section = (
                f'<div class="pred-callout"><strong>Predicted (G14):</strong>{r["pred_html"]}</div>'
                if r["pred_html"]
                else ""
            )
            rec_html += f"""
            <article class="rec-card">
              <h3>
                <span class="num">{r['num']}</span>
                <span style="flex:1">{escape(r['title'])}</span>
                <span class="verdict {r['verdict_class']}">{escape(r['verdict'])}</span>
              </h3>
              {pred_section}
              <details>
                <summary>Mechanism · pillars · pre-mortem · next step</summary>
                <div class="body-html">{r['body_html']}</div>
              </details>
            </article>
            """
        rec_html += "</div>"
    else:
        rec_html = '<p><em>No recommendations parsed for this week.</em></p>'

    # Open predictions table
    if predictions["open"]:
        rows_html = ""
        for p in predictions["open"]:
            rows_html += (
                f"<tr>"
                f"<td>{escape(p.get('recommendation_id', ''))}</td>"
                f"<td>{escape(p.get('title', ''))}</td>"
                f"<td>{escape(p.get('predicted_metric', ''))}</td>"
                f"<td>{escape(str(p.get('predicted_delta', '')))}</td>"
                f"<td>{escape(str(p.get('predicted_window_days', '')))}</td>"
                f"<td>{escape(p.get('predicted_due_at', ''))[:10]}</td>"
                f"</tr>"
            )
        pred_table_html = f"""
        <table>
          <thead>
            <tr><th>Rec ID</th><th>Title</th><th>Metric</th><th>Delta</th><th>Window (d)</th><th>Due</th></tr>
          </thead>
          <tbody>{rows_html}</tbody>
        </table>
        """
    else:
        pred_table_html = "<p><em>No open predictions.</em></p>"

    # Analyses
    analyses_html = ""
    for slug, title, html in analyses:
        analyses_html += f"""
        <details class="analysis-card" id="{escape(slug)}">
          <summary>{escape(title)}</summary>
          <div>{html}</div>
        </details>
        """

    # Sidebar
    sidebar_html = '<h2>This week</h2><ul>'
    sidebar_html += '<li><a href="#brief">Executive Brief</a></li>'
    sidebar_html += '<li><a href="#recs">Top 3 Recommendations</a></li>'
    sidebar_html += '<li><a href="#predictions">Predictions Tracker</a></li>'
    sidebar_html += '<li><a href="#analyses">Supporting Analyses</a></li>'
    sidebar_html += '<li><a href="#contradictions">Contradictions</a></li>'
    sidebar_html += '</ul>'
    sidebar_html += '<h2>Analyses</h2><ul>'
    for slug, title, _ in analyses:
        sidebar_html += f'<li><a href="#{escape(slug)}">{escape(title)}</a></li>'
    sidebar_html += '</ul>'
    if all_weeks:
        sidebar_html += '<h2>Archive</h2><ul class="week-nav">'
        for w in all_weeks[:24]:
            link = (
                "index.html" if w == all_weeks[0] else f"archive/{w}.html"
            )
            cls = ' style="font-weight:700"' if w == week_id else ''
            sidebar_html += f'<li><a href="{link}"{cls}>{w}</a></li>'
        sidebar_html += '</ul>'
    sidebar_html += '<h2>Source</h2><ul><li><a href="https://github.com/deepakp1308/mailchimp-growth-strategist" target="_blank" rel="noopener">GitHub repo</a></li></ul>'

    # Brief markdown for the body fallback (above the fold = SCQA + recs already extracted)
    brief_html = render_md(brief_md)

    # Contradictions
    contradictions_html = render_md(contradictions_md) if contradictions_md else "<p><em>No active contradictions.</em></p>"

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Mailchimp Growth Strategist — {week_id}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
</head>
<body>
<div class="layout">
  <nav class="sidebar">
    <div style="font-weight:700;font-size:14px;margin-bottom:6px">Mailchimp<br>Growth Strategist</div>
    <div style="color:var(--muted);font-size:12px;margin-bottom:18px">Week {week_id}</div>
    {sidebar_html}
  </nav>

  <main>
    <div class="title-block">
      <h1>Executive Report — {week_id}</h1>
      <div class="subtitle">
        Mailchimp Growth Strategist Agent
        · prepared for Deepak Prabhakaran
        · {generated_at}
      </div>
    </div>

    <div class="hit-rate-card">
      <div>
        <div style="font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em">Rolling 12-week prediction hit rate</div>
        <div style="margin-top:6px">{rate_html}</div>
      </div>
    </div>

    <section id="brief" class="scqa">
      <h2>SCQA — Situation · Complication · Question · Answer</h2>
      {scqa_html}
    </section>

    <section id="recs" class="recs">
      <h2>Top 3 Recommendations</h2>
      {rec_html}
    </section>

    <section id="predictions" class="predictions">
      <h2>Falsifiable Predictions Tracker (G14)</h2>
      <p style="color:var(--muted)">Every recommendation makes a falsifiable prediction. Each prediction is graded once its window elapses; recommendations from low-accuracy subagents get auto-downgraded confidence (pattern borrowed from <a href="https://github.com/karpathy/autoresearch" target="_blank" rel="noopener">karpathy/autoresearch</a>'s val_bpb feedback loop).</p>
      <h3 style="font-size:16px;margin-top:18px">Open predictions (awaiting their window)</h3>
      {pred_table_html}
    </section>

    <section id="analyses" class="analyses">
      <h2>Supporting Analyses</h2>
      <p style="color:var(--muted)">Each analysis is produced by a specialized subagent. Click to expand.</p>
      {analyses_html}
    </section>

    <section id="contradictions" class="contradictions">
      <h2>Contradictions Ledger</h2>
      <p style="color:var(--muted)">Per Plan G6/G9, every conflict between sources is logged here — never silently resolved.</p>
      {contradictions_html}
    </section>

    <div class="footer">
      <strong>About this report.</strong> Generated by the Mailchimp Growth Strategist multi-agent system —
      orchestrator + 17 specialist subagents (4 ingestion, 5 diagnostic, 2 synthesis, 4 QC, 1 meta).
      Architecture follows Anthropic's 2026 hierarchical planner-executor pattern with adversarial-dual-analysis QC.
      The agent reads <code>program.md</code> and <code>predictions-ledger.jsonl</code> first on every run.
      Pre-commit hook enforces 3-tier file access separation (human-only / append-only / agent-editable).
      <br><br>
      <a href="https://github.com/deepakp1308/mailchimp-growth-strategist" target="_blank" rel="noopener">Source on GitHub</a>
      · <a href="https://github.com/deepakp1308/mailchimp-growth-strategist/tree/main/analyses/{week_id}" target="_blank" rel="noopener">Raw analyses for {week_id}</a>
      · Built with markdown {markdown.__version__ if MD_AVAILABLE else 'fallback'}.
    </div>
  </main>
</div>
</body>
</html>
"""


def main() -> int:
    week_id = sys.argv[1] if len(sys.argv) > 1 else current_iso_week()
    analyses_dir = REPO_ROOT / "analyses"
    week_dir = analyses_dir / week_id

    if not week_dir.exists():
        print(f"WARN: {week_dir} does not exist; generating empty report", file=sys.stderr)
        week_dir.mkdir(parents=True, exist_ok=True)

    all_weeks = list_archive_weeks(analyses_dir)
    html = build_html(week_id, week_dir, all_weeks)

    out_path = REPO_ROOT / "dashboards" / "index.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html)

    archive = REPO_ROOT / "dashboards" / "archive" / f"{week_id}.html"
    archive.parent.mkdir(parents=True, exist_ok=True)
    archive.write_text(html)

    # Also dump the raw structured data for downstream consumers
    data_path = REPO_ROOT / "dashboards" / "_data" / f"{week_id}.json"
    data_path.parent.mkdir(parents=True, exist_ok=True)
    predictions = load_predictions(REPO_ROOT / "predictions-ledger.jsonl")
    findings = load_findings_summary(REPO_ROOT / "findings-ledger.jsonl", week_id)
    data_path.write_text(
        json.dumps(
            {
                "week_id": week_id,
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "predictions": predictions,
                "findings": findings,
            },
            indent=2,
            default=str,
        )
    )

    print(f"Report generated:")
    print(f"  {out_path}  ({out_path.stat().st_size:,} bytes)")
    print(f"  {archive}")
    print(f"  {data_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
