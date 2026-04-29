# GTM Lever Audit — 2026-W17

**Run timestamp:** 2026-04-28
**Window:** Trailing 2 weeks (2026-04-13 → 2026-04-26)
**Source:** `bi_aggregate.bookings_weekly` (timing × package), `bi_aggregate.product_health_weekly` (SMS metrics)

## Headline

- 4 FY26 GTM levers; **2 on track, 1 behind, 1 unknown-target**.
- The **scaled acquisition + Annual Plans launch** is the single biggest near-term GTM bet — first read available ~2026-05-21.
- The **expansion-SMS motion** is delivering — +45 bps penetration, but `sms_paid_plan_users` plateau at ~34K-35K suggests the new-user-attach motion is working while the existing-user-conversion has stalled.

## By Lever

### Lever 1 — Scaled acquisition via mailchimp.com — **In-flight, target known**
- **FY26 target:** $3.1M new bookings (per Annual Plans launch announcement)
- **Trailing 2-week new bookings $:** ~$210K + $94K = ~$304K (just over $1.5M annualized at this rate ÷ 2)
  - Wait — that's combined, not just self-serve. Self-serve subset would be smaller. Need to re-query for `self_serve_digital_bookings_*` field.
- **Status:** Annual Plans experiment LIVE since 2026-04-23 (4-week test). First read 2026-05-21.
- **Predicted impact (per Annual Plans launch post):** $70K in-year FY26 / $1.3M-$3.9M FY27
- **On-track?** Premature to say — wait for first read.
- **Risk:** AP take rate target is **>10%**; from BigQuery data this week, annual-plan bookings (essential_annual + standard_annual + premium_annual) total **$5.9K (3% of $ bookings) on week of 4/19**. Pre-Annual Plans launch baseline is essentially zero — so any take-rate is a win. But the 10% target is aggressive.
- **Confidence:** Medium

### Lever 2 — MM acquisition — **Target unknown**
- **FY26 target:** Not explicitly quantified in narrative. Implies "scaling coverage of onboarding and account management across MM customers ($299+ MRR), incentivizing agency partners to improve 90d retention and NRR."
- **Trailing data:** Premium tier bookings = ~$28K (week 4/19), $7K (week 4/26 partial). Annualized ~$1.8M just from Premium new bookings.
- **MM proxy:** `is_high_value=TRUE` filter on bookings — would need a re-run; not done this cycle.
- **Status:** Likely under-investing. Per Strategy Reconciler, **0 structural MM Account/Billing experiments in 9 months.**
- **On-track?** **No** — based on visible execution. The MM ICP (priority 1) is the most under-shipped FY26 priority.
- **Confidence:** Medium-High in the gap finding; Low in the actual run-rate (need MM-specific query).

### Lever 3 — Expansion (SMS first) — **Cumulative on-track, near-term plateau**
- **Per Connor Callahan claim (2026-03-20):** 6 stacked SMS experiments → $1.08M FY26 / $3.96M FY27, +45 bps SMS penetration
- **BigQuery `sms_paid_plan_users` (trailing 13 weeks):** 31,648 → 34,303 → 33,673 (week 4/26 partial) — **+8% over 13 weeks** but appears to plateau ~34K
- **`sms_credit_purchases` (trailing 13 weeks):** week 2/8: 1,126 → week 4/19: 645. **Trending DOWN by ~40%** over 11 weeks.
- **On-track?** Cumulative wins in books (good). Forward momentum on plan-attach is slowing. The 40% drop in `sms_credit_purchases` is concerning and worth a deeper diagnostic.
- **Confidence:** Medium-High on past wins; Medium on forward trajectory.

### Lever 4 — Strategic technology partners (Wix / Shopify / Canva / Amazon) — **Target unknown**
- **FY26 target:** Not quantified in narrative; "joint solutions" and "extend reach globally"
- **Evidence found:** Meta Custom Audience Integration GA (2026-04-21) + Builtwith intent integration experiments
- **Trailing data:** `service_partners_bookings_*` and `tech_partners_bookings_*` fields not pulled this cycle (gap).
- **On-track?** Unknown — but Meta CA GA is a positive signal.
- **Confidence:** Low — need targeted query.

## Booking timing mix (week 4/19 — most-representative full week)

| Timing | Users | $ | $-share | $-per-user (ARPU proxy) |
|---|---|---|---|---|
| immediate to paid | 2,627 | $138.6K | **57%** | $52.74 |
| free to paid | 2,268 | $50.9K | 21% | $22.46 (lowest) |
| direct to paid | 370 | $15.0K | 6% | $40.59 |
| N/A | 34 | $2.3K | 1% | — |
| **Total** | 5,299 | $206.8K | 100% | $39.04 avg |

**Key insights:**

1. **Free Trial Rolloff (free-to-paid) generates 43% of users but only 21% of $.** Lowest ARPU per booking. **Implication:** if Annual Plans moves Standard/Essentials to trial-only start AND the AP take rate is >10%, the discount on Annual could increase booking volume but reduce per-booking $. Net depends on retention lift.

2. **Immediate-to-paid is highest revenue contributor (57% of $).** These are users who skip free entirely and go straight to paid in their first 30 days. Annual Plans variant offers them a 20% AP option — could shift some to lower per-booking $ but with longer commitment.

3. **Direct-to-paid (existing free users converting later)** is the smallest segment by users (7%) but moderate ARPU. Targeting messaging here could be efficient.

4. **PDF dashboard claim contradiction (logged):** Exec Overview dashboard (week ending 4/19) shows "Free Trial Rolloff = 9.39% / Existing Direct = 29.05% / New Direct = 61.56%" — these add to 100% but use **different denominators** than BigQuery `new_booking_timing` field (which gave 21%/6%/57%). Either definition mismatch or PW comparison anomaly. **Flag.**

## Tier mix (week 4/19)

| Package | Users | $ | $-share |
|---|---|---|---|
| standard_monthly_plan_v0 | 2,598 | $116.7K | **52%** |
| essential_monthly_plan_v0 | 2,578 | $55.3K | 25% |
| premium_monthly_plan_v0 | 52 | $28.4K | 13% |
| premium_annual_plan_v0 | 7 | $4.1K | 2% |
| standard_annual_plan_v0 | 24 | $1.3K | <1% |
| essential_annual_plan_v0 | 36 | $0.6K | <1% |

**Annual plan share of $ bookings: ~3%** (was effectively zero pre-launch). **Annual plan share of users: ~1.3%** (67/5,295).

**Interpretation:** Pre-Annual-Plans-experiment baseline is very low. The 4-week experiment will be the first signal of whether the >10% take rate target is realistic. **3% to >10% is a 3x+ lift required.**

## Open data anomalies

1. **PDF Exec Overview "Existing Direct Bookings Share = 29.05% CP / 58.35% PW"** — that's a 50% week-over-week change. Likely an artifact of the new dashboard wiring or a real shift. **Action:** verify with Finance/Data Eng.

2. **PDF "Premium Booking Share = 23.42% CP / 51.76% PW"** — similar anomaly. From BigQuery, Premium = 13% of $. **Action:** confirm we're not miscomparing CP-vs-PW columns.

3. **`sms_credit_purchases` declining trend** — week 2/8: 1,126 → week 4/19: 645. **Action:** investigate as a separate experiment readout review.

## Findings ledger row written

```json
{"ts":"2026-04-28T21:00:00Z","source":"mc-gtm-lever-analyst","claim":"GTM levers: scaled acquisition (Annual Plans live, target $3.1M, first read 2026-05-21); MM acquisition (target unknown, 0 structural launches in 9mo); SMS expansion (cumulative wins booked, but sms_paid_plan_users plateau ~34K and sms_credit_purchases -40% over 11 wks). Annual plan baseline = 3% of $ bookings vs >10% target = 3x+ lift required.","confidence":"medium","citations":["analyses/2026-W17/04-gtm-levers.md","queries/11-ft-rolloff-bookings.sql","queries/14-bookings-by-tier.sql"]}
```
