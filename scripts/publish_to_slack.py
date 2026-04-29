#!/usr/bin/env python3
"""
Publish the executive brief to Slack DM (W8FL6URHQ = Deepak).

Strategy: this script just *prepares* the payload. Sending happens via the
Slack MCP from inside Cursor (so we leverage the agent's existing auth).

Usage:
  python3 scripts/publish_to_slack.py [YYYY-WW]
  -> writes /tmp/mc-growth-slack-payload.txt + prints summary

Then the agent invokes:
  slack_send_message(channel="W8FL6URHQ", text=<payload>)
"""

import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_DM_USER = "W8FL6URHQ"  # Deepak per canon/org-glossary.md
# Live as of 2026-04-29 — see https://github.com/deepakp1308/mailchimp-growth-strategist
DASHBOARD_BASE = os.environ.get(
    "MC_GROWTH_DASHBOARD_URL",
    "https://deepakp1308.github.io/mailchimp-growth-strategist/",
)
ARCHIVE_BASE = DASHBOARD_BASE.rstrip("/") + "/archive/"


def current_iso_week() -> str:
    y, w, _ = datetime.now(timezone.utc).isocalendar()
    return f"{y}-W{w:02d}"


def excerpt_brief(brief_md: str, max_lines: int = 60) -> str:
    """Pull the headline + top-3 recommendations + hit rate summary."""
    lines = brief_md.splitlines()
    out = []
    in_top3 = False
    rec_count = 0
    for line in lines:
        if line.startswith("## SCQA"):
            in_top3 = True
        if in_top3:
            out.append(line)
        if line.startswith("### #"):
            rec_count += 1
            if rec_count > 3:
                break
        if len(out) >= max_lines:
            out.append("\n*(truncated — see full brief on dashboard)*")
            break
    return "\n".join(out) if out else brief_md[:2000]


def main() -> int:
    week_id = sys.argv[1] if len(sys.argv) > 1 else current_iso_week()
    week_dir = REPO_ROOT / "analyses" / week_id
    brief_path = week_dir / "00-executive-brief.md"

    if not brief_path.exists():
        print(f"ERROR: {brief_path} does not exist. Run the orchestrator first.", file=sys.stderr)
        return 1

    brief_md = brief_path.read_text()
    excerpt = excerpt_brief(brief_md)

    payload = (
        f"*Mailchimp Growth Strategist — {week_id}*\n"
        f"\n"
        f"{excerpt}\n"
        f"\n"
        f"*Full brief & dashboard*: {DASHBOARD_BASE}\n"
        f"*This week's analyses*: `analyses/{week_id}/`\n"
    )

    out_path = Path("/tmp/mc-growth-slack-payload.txt")
    out_path.write_text(payload)

    print(f"Slack payload prepared at: {out_path}")
    print(f"Recipient: {DEFAULT_DM_USER}")
    print(f"Length: {len(payload)} chars")
    print()
    print("--- PAYLOAD PREVIEW ---")
    print(payload[:1200])
    print("--- END PREVIEW ---")
    print()
    print("Agent: invoke Slack MCP to send this. e.g.:")
    print(f"  slack_send_message(channel='{DEFAULT_DM_USER}', text=<contents of {out_path}>)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
