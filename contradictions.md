# Contradictions Ledger

> **Purpose:** Per Guardrail G6 + G9, every conflict between sources or between this week's claim and a prior ledger entry **must** be logged here. Never silently resolved.
>
> **Format:** newest-first. Each entry includes: detection time, claim A, claim B, sources, magnitude, resolution (with rationale), confidence.

## Schema

```
## YYYY-MM-DD HH:MM (detector: <subagent-name>)
**Topic:** <one-line topic>
**Claim A:** <statement> — Source: <link/file/Slack TS>
**Claim B:** <conflicting statement> — Source: <link/file/Slack TS>
**Magnitude:** <e.g. 2.3% delta on Active Churn Rate; ~$200K MRR>
**Resolution:** <BigQuery picked as canon / Finance picked as canon / Unresolved-pending-DRI>
**Rationale:** <why>
**Confidence:** <High / Medium / Low>
**Open?** <yes / no — if yes, attach Slack escalation TS once raised>
```

## Active contradictions

## 2026-04-28 21:00 (detector: mc-cohort-churn-diagnostician)
**Topic:** Annualization of weekly churn rate
**Claim A:** Active weekly churn rate 0.95% per Exec Overview dashboard (week ending 2026-04-19)
**Claim B:** Annualized active churn from `bi_aggregate.churn_daily` cohort summation = ~$26.5M / total annualized order amount
**Magnitude:** Different units — weekly flow-rate vs annualized cohort-loss MRR. Trivial weekly × 52 dramatically overstates annual churn.
**Resolution:** BigQuery-derived $ values are the source of truth for $-at-risk; weekly rate dashboards are flow-rates, NOT cohort-loss-rates. Picked BigQuery as canon for this report.
**Rationale:** BigQuery has finer-grained cohort cuts; dashboard rates are presentation-layer simplifications.
**Confidence:** Medium — should reconcile with Finance methodology
**Open?** Yes — flag for next cycle to confirm with Finance team

## 2026-04-28 21:00 (detector: mc-gtm-lever-analyst)
**Topic:** Booking timing share — PDF dashboard vs BigQuery `new_booking_timing` field
**Claim A:** Exec Overview dashboard (week ending 2026-04-19): Free Trial Rolloff = 9.39% / Existing Direct = 29.05% / New Direct = 61.56%
**Claim B:** From `bi_aggregate.bookings_weekly` for week 2026-04-19: free_to_paid = 21% of $ (or 43% of users); direct_to_paid = 6% of $ (or 7% of users); immediate_to_paid = 57% of $ (or 50% of users)
**Magnitude:** Different denominators — PDF appears to be % of bookings users; BigQuery returns both users and $ shares. Doesn't fully reconcile even on user-share basis (PDF says 9.39% FT rolloff / BigQuery says 43%).
**Resolution:** UNRESOLVED — likely the PDF dashboard uses a different `new_booking_timing` definition or filters out N/A timings differently. **Action:** verify with Finance/Data Eng team next cycle.
**Confidence:** Medium — needs explicit reconciliation
**Open?** Yes — open until resolved with Finance

## Resolved contradictions (archive)

*(none yet)*
