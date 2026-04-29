#!/usr/bin/env bash
# Cursor sessionStart hook — checks if it's time for a weekly run.
#
# Reads JSON from stdin (Cursor passes context). Writes a JSON response to
# stdout that injects context into the agent's session if a run is due.
#
# Triggers a nudge when:
#   - Today is Monday OR today is later in the week, AND
#   - Most recent analyses/<YYYY-WW>/00-executive-brief.md is >5 days old
#     (or doesn't exist).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
ANALYSES="$REPO_ROOT/analyses"

# Discard stdin (Cursor will send context JSON; we don't need it for this nudge)
cat > /dev/null

# Find the most recent executive brief
LATEST_BRIEF=""
LATEST_AGE_DAYS=999

if [ -d "$ANALYSES" ]; then
  while IFS= read -r f; do
    if [ -f "$f" ]; then
      AGE_SECONDS=$(( $(date +%s) - $(stat -f %m "$f" 2>/dev/null || stat -c %Y "$f") ))
      AGE_DAYS=$(( AGE_SECONDS / 86400 ))
      if [ "$AGE_DAYS" -lt "$LATEST_AGE_DAYS" ]; then
        LATEST_AGE_DAYS=$AGE_DAYS
        LATEST_BRIEF="$f"
      fi
    fi
  done < <(find "$ANALYSES" -name "00-executive-brief.md" -type f 2>/dev/null)
fi

# Decide whether to nudge
DAY_OF_WEEK=$(date +%u)   # 1 = Monday
NUDGE="false"

if [ "$LATEST_AGE_DAYS" -ge 5 ]; then
  NUDGE="true"
elif [ "$DAY_OF_WEEK" = "1" ] && [ "$LATEST_AGE_DAYS" -ge 3 ]; then
  NUDGE="true"
fi

if [ "$NUDGE" = "true" ]; then
  ISO_WEEK=$(date +%G-W%V)
  cat <<EOF
{
  "addContext": "Weekly Mailchimp Growth Strategist run is due (last brief was \${LATEST_AGE_DAYS} days ago). When you're ready, invoke: 'Run mailchimp-growth-strategist orchestrator for $ISO_WEEK following Mode A'."
}
EOF
else
  echo "{}"
fi

exit 0
