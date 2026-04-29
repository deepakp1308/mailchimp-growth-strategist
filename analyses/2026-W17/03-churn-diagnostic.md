# Cohort Churn Diagnostic — 2026-W17

**Run timestamp:** 2026-04-28
**Window:** 2026-04-13 → 2026-04-26 (trailing 2 weeks)
**Source data:** `bi_aggregate.churn_daily` (cohort × package and × tenure pulls)

## Headline

- **Trailing 2-week active churn $:** ~$1.02M (annualized ~**$26.5M**)
- **Trailing 2-week passive churn $:** ~$1.93M (annualized ~**$50.0M**)
- **Total annualized MRR-at-risk:** **~$76.5M**
- **FY26 churn-reduction target:** $14.9M (per Annual Plans launch announcement, Slack TS 1776958294)
- **Implied required reduction:** **~20% of total annualized MRR-at-risk** OR **~30% of active+passive MRR-at-risk excluding "legacy monthly" billing failures**

> Important caveat: MRR-at-risk ≠ MRR-lost. Many at-risk customers are saved by retention/winback motions. A reasonable working assumption is 50%-65% conversion from at-risk to actually-lost. Even at 50%, $76.5M annualized at-risk → ~$38M annualized actual lost MRR.

## Top-3 worst cohorts by Active Churn $

### #1 — Standard tier (`standard_monthly_plan_v0`)
- **Active MRR at risk (biweekly):** $461,273
- **Passive MRR at risk (biweekly):** $775,523 (largest passive bucket)
- **Total biweekly:** $1.24M → **annualized ~$32.2M**
- **Users at risk per week:** ~3,264 active + ~4,440 passive = ~7,700/week
- **FY26 bets that address:** Annual Plans (live since Apr 23 — moves Standard to trial-only start), Personalization/Joins Segment (reduces automation-driven churn ~10% of HVC churners per 2023 report)
- **Recommendation hint:** Standard tier is where churn $ is concentrated AND where the new-user funnel converges. Annual Plans + retention-prediction analytics are the right bets.

### #2 — Essentials tier (`essential_monthly_plan_v0`)
- **Active MRR at risk (biweekly):** $212,635
- **Passive MRR at risk (biweekly):** $285,450
- **Total biweekly:** $498K → **annualized ~$13.0M**
- **Users at risk per week:** ~2,554 active + ~2,974 passive = ~5,528/week
- **FY26 bets that address:** OTP-at-activation (just landed, +3.74% activation rate), Annual Plans (Essentials moves to trial-only start in experiment)
- **Recommendation hint:** Essentials is the "value tier"; price-sensitive churners. Annual Plans 14-day FT + 20% AP discount is exactly the right shape.

### #3 — Legacy Monthly (`legacy monthly`)
- **Active MRR at risk (biweekly):** $156,288
- **Passive MRR at risk (biweekly):** $485,549 (very large — billing failure heavy)
- **Total biweekly:** $642K → **annualized ~$16.7M**
- **Users at risk per week:** ~423 active + ~949 passive = ~1,371/week
- **FY26 bets that address:** **NONE explicit.** This is grandfathered customers on legacy plans where billing failures dominate. **GAP**: no FY26 priority specifically targets billing-failure recovery for legacy plans.
- **Recommendation hint:** This is a quiet $16M annualized at-risk pile that is invisible in the FY26 narrative. Worth a dedicated investigation — possibly low-cost, high-leverage (better dunning, payment-method update workflows).

## Top-3 worst cohorts by Tenure

### #1 — `24+` months tenure
- **Active MRR at risk (biweekly):** **$690,746** (largest single tenure cohort)
- **Passive MRR at risk (biweekly):** $1,507,379 (also largest)
- **Total biweekly:** $2.20M → **annualized ~$57.2M** (the dominant tenure bucket — 75% of MRR-at-risk)
- **Users at risk per week:** ~3,956 active + ~5,568 passive = ~9,524/week
- **FY26 bets that address:** Annual Plans (longer commitment locks in tenured), MM Account/Billing flex (long-tenure customers most likely MM-shaped), Place of Supply tax compliance (compliance-driven retention)
- **Counterintuitive insight:** FY26 narrative emphasizes "6-month new-user churn = 43%" but **the actual MRR exposure is in 24+ tenure**. New-user churn is high in % terms but low in absolute $. Long-tenure customers have higher ARPU and being lost is more painful.

### #2 — `<24` months tenure
- **Active MRR at risk (biweekly):** $117,679
- **Passive MRR at risk (biweekly):** $189,931
- **Total annualized:** ~$8.0M
- **FY26 bets that address:** Annual Plans, Personalization (CDP-driven retention experiments)

### #3 — `<12` months tenure
- **Active MRR at risk (biweekly):** $80,248
- **Passive MRR at risk (biweekly):** $99,677
- **Total annualized:** ~$4.7M

## Cohorts NOT addressed by FY26 (gaps)

| Cohort | Annualized $ at risk | Why no FY26 priority maps |
|---|---|---|
| Legacy monthly (passive billing failures) | ~$13M (passive only) | No explicit "legacy plan migration" or "dunning improvement" priority |
| Free → cancellation (`free` package, $75K active + $68K passive) | ~$3.7M | Free churn is structural; FY26 does not target free retention |
| `<1 month` tenure cohort (very early dropoff) | ~$0.9M | New-user activation work (OTP) addresses indirectly |

## Cross-check vs % Churn Overview.xlsx

> **Status:** unable to fully cross-check — the xlsx was not parsed in this run (openpyxl install required). Logged to follow up.

Tableau dashboard references (from PDF parse, week ending 2026-04-19):
- Active Churn Rate (CP weekly): 0.95%
- Passive Churn Rate (CP weekly): 0.45%
- Total Churn Rate (CP weekly): 1.54% (Excel-aligned with Finance per Annual Plans launch text)

Implied annualized churn rate (using simple weekly × 52, ignoring compounding): ~80% — which is clearly too high; the dashboard rates are weekly-flow rates, NOT cohort-loss rates. This is an **important contradiction** to flag (logged below).

## Contradictions logged

```markdown
## 2026-04-28 21:00 (detector: mc-cohort-churn-diagnostician)
**Topic:** Annualization of weekly churn rate
**Claim A:** Active weekly churn rate 0.95% (per Exec Overview dashboard, 2026-04-19)
**Claim B:** Annualized active churn from `bi_aggregate.churn_daily` = ~$26.5M / total annualized order amount
**Magnitude:** mismatch in interpretation — weekly rate × 52 dramatically overstates annual churn
**Resolution:** BigQuery-derived $ values are the source of truth for $-at-risk; weekly rate dashboards are flow-rates, NOT cohort-loss-rates. They cannot be trivially annualized.
**Confidence:** Medium — should reconcile with Finance methodology
**Open?** Yes — flag in executive brief Open Questions
```

## Findings ledger row written

```json
{"ts":"2026-04-28T21:00:00Z","source":"mc-cohort-churn-diagnostician","claim":"Annualized MRR-at-risk = ~$76.5M (active+passive); concentrated in (a) Standard tier $32M, (b) 24+ tenure $57M (75% of total). FY26 $14.9M reduction target is realistic only if Annual Plans, churn-prediction analytics, and legacy-plan dunning all hit. Legacy-monthly cohort ($16M annualized at-risk) is invisible in FY26 narrative.","confidence":"medium","citations":["analyses/2026-W17/03-churn-diagnostic.md","queries/40-cohort-churn-by-package.sql","queries/41-cohort-churn-by-tenure.sql"]}
```
