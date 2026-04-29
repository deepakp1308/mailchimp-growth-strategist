#!/usr/bin/env bash
# Weekly orchestration entrypoint.
#
# Run this script (manually or via Cursor hook on Mon 7am PT) to trigger the
# full Mailchimp Growth Strategist pipeline for the current ISO week.
#
# This script is the *deterministic* shell layer. The agent intelligence
# happens inside Cursor when the orchestrator skill (mailchimp-growth-strategist)
# is invoked. This script's job:
#   1. Sanity-check the repo state.
#   2. Compute current ISO week.
#   3. Prep workdirs.
#   4. Print the orchestrator-invocation prompt to stdout (for the operator
#      OR for a Cursor hook to feed to `cursor agent`).
#
# It does NOT directly call BigQuery / Slack / etc. The agent does that.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

# Compute ISO week
YEAR_WEEK=$(date -u +%G-W%V)
ANALYSES_DIR="analyses/$YEAR_WEEK"
mkdir -p "$ANALYSES_DIR" "$ANALYSES_DIR/_canon_drafts"

# Sanity checks
if [ ! -f "program.md" ]; then
  echo "ERROR: program.md missing. Run from a properly scaffolded repo." >&2
  exit 1
fi

if [ ! -d "canon" ] || [ ! -d "queries" ]; then
  echo "ERROR: canon/ or queries/ missing." >&2
  exit 1
fi

# Print orchestrator invocation
cat <<EOF
==================================================================
MAILCHIMP GROWTH STRATEGIST — WEEKLY RUN  ($YEAR_WEEK)
==================================================================

Repo: $REPO_ROOT
Output dir: $REPO_ROOT/$ANALYSES_DIR

To run from Cursor, invoke:

  cursor agent "run mailchimp-growth-strategist for $YEAR_WEEK"

Or paste this prompt into a Cursor chat (the orchestrator skill
will be auto-loaded by description match):

  > Run the mailchimp-growth-strategist orchestrator for week $YEAR_WEEK.
  > Output target: $ANALYSES_DIR/
  > Follow Mode A (full weekly run) per SKILL.md.

After completion:
  python3 scripts/generate_dashboard.py $YEAR_WEEK
  python3 scripts/publish_to_slack.py $YEAR_WEEK

==================================================================
EOF
