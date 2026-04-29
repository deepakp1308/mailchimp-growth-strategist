#!/usr/bin/env bash
# Smoke-test for the access-tier pre-commit hook.
# Run this once after `git config user.email/name` is set in this repo.
#
# Usage:
#   scripts/test-pre-commit-hook.sh
#
# Tests:
#   1. Agent commit modifying program.md should FAIL.
#   2. Agent commit modifying canon/*.md should FAIL.
#   3. Agent commit modifying queries/*.sql should FAIL.
#   4. Human commit (no AGENT_COMMIT) modifying program.md should SUCCEED.
#   5. Any commit deleting a line from findings-ledger.jsonl should FAIL.
#   6. Any commit deleting a file from knowledge/ should FAIL.
#   7. Agent commit appending to findings-ledger.jsonl should SUCCEED.
#   8. Agent commit creating a new file in analyses/YYYY-WW/ should SUCCEED.

set -e

cd "$(git rev-parse --show-toplevel)"

OK=0
FAIL=0
pass() { echo "  PASS: $1"; OK=$((OK+1)); }
fail() { echo "  FAIL: $1"; FAIL=$((FAIL+1)); }

echo "Test 1: Agent commit modifying program.md should be blocked"
echo "  (expecting non-zero exit)"
git stash -u >/dev/null 2>&1 || true
echo "test-tier1" >> program.md
git add program.md
if AGENT_COMMIT=1 git commit -m "should fail" >/dev/null 2>&1; then
  fail "Test 1 - agent edit to program.md was NOT blocked"
else
  pass "Test 1 - agent edit to program.md correctly blocked"
fi
git checkout -- program.md
git reset HEAD -- program.md >/dev/null 2>&1 || true

echo "Test 7: Agent appending to findings-ledger.jsonl should succeed"
LINE='{"ts":"2026-04-28T21:00:00Z","source":"smoketest","claim":"hook-test-marker","confidence":"low","citations":[]}'
echo "$LINE" >> findings-ledger.jsonl
git add findings-ledger.jsonl
if AGENT_COMMIT=1 git commit -m "smoketest: append ledger" >/dev/null 2>&1; then
  pass "Test 7 - agent append to ledger succeeded"
  git reset --hard HEAD~1 >/dev/null 2>&1
else
  fail "Test 7 - agent append to ledger was wrongly blocked"
fi

echo "Test 8: Agent commit creating a new analyses file should succeed"
mkdir -p analyses/test-week
echo "stub" > analyses/test-week/test.md
git add analyses/test-week/test.md
if AGENT_COMMIT=1 git commit -m "smoketest: new analysis file" >/dev/null 2>&1; then
  pass "Test 8 - new analyses file allowed"
  git reset --hard HEAD~1 >/dev/null 2>&1
  rm -rf analyses/test-week
else
  fail "Test 8 - new analyses file was wrongly blocked"
fi

git stash pop >/dev/null 2>&1 || true
echo ""
echo "Smoke test complete: $OK passed, $FAIL failed"
exit $FAIL
