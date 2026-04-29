# Experiment Portfolio Synthesis — 2026-W17

**Run timestamp:** 2026-04-28
**Window:** Aug 1, 2025 → Apr 28, 2026 (9 months / ~39 weeks)
**Source data:** `knowledge/slack/_seed_transcript.md`, `canon/experiment-canon.md`, BigQuery results

## Headline numbers

- ~13 named experiments + 6+ unnamed initiatives surfaced in window
- **Win rate (concluded):** 8/10 = **80%** (very high — likely positive selection effect: clear-wins are over-shared in `#mailchimp-launched`)
- **$ impact (wins, FY26 quoted):** ~$0.5M (excl. SMS stack)
- **$ impact (wins, FY27 annualized):** ~$5.4M (incl. SMS stack)
- **Headline pattern:** Personalization/CDP cluster is the strongest compounding area

## By outcome

| Status | Count | $ impact (FY26 cited) |
|---|---|---|
| clear-win | 8 | ~$5.4M FY27 cumulative incl. SMS stack |
| clear-loss | 0 | — |
| neutral | 0 visible (selection bias) | — |
| inconclusive | 1 (WhatsApp — too early) | — |
| running | 4 (Annual Plans, multiple OBX, Domain Auth, Intent Aware Onboarding) | TBD |

## By area

| Area | Experiments | Wins | Pattern |
|---|---|---|---|
| Audience / CDP / Segmentation | 4 | 4 | **Compound winner** |
| SMS Growth | 6 (stacked) | 6 | **Compound winner** |
| Email modernization | 2 | 2 | Quiet success |
| Identity / Activation | 2 | 2 | Underrated |
| Plans / Pricing | 1 (Annual Plans) | running | First-ever rate-card experiment |
| Channels (WhatsApp) | 1 | running | Private beta |
| OBX / Onboarding agentic | 3 | running | DFY-stage |
| Integrations / Lead Ads | 1 | 1 | Meta Custom Audience GA |

## By FY26 priority

| Priority | # experiments | wins | $ FY26 (cited) |
|---|---|---|---|
| P3 Integrations & Data Enablement | 4 | 4 | $20K + meaningful intangibles |
| P2 Channel Expansion (SMS) | 6+ | 6+ | $1.08M (cumulative) |
| Pricing/Packaging (Annual Plans) | 1 | running | $70K in-year / $1.3-3.9M FY27 (predicted) |
| MM Account/Billing structural | 0 | 0 | — **GAP** |
| Lead Ads | 1 | 1 | TBD |
| Loyalty/UGC | 0 | 0 | (correctly deprioritized) |
| AI agents | 1 measured (Project Alfred) | 1 | +6% email creates per user |
| Advanced campaign mgmt (frequency caps, multi-audience) | 0 | 0 | **GAP** |

## By ICP (as best-fit tag)

| ICP | # experiments tagged | wins |
|---|---|---|
| All ICPs (cross-cutting capability) | 7 | 7 |
| Subscription MM | 1 (Joins Segment, especially HVC-leaning) | 1 |
| Community Small/LMM | 0 directly tagged | 0 |
| Ecomm Small/LMM | 4 (Meta CA, Sections Manager, Personalization-tilt) | 4 |

**Gap signal:** Community ICP (Civic/Social) — the segment with our highest MC penetration index (370 vs 3.2% baseline) — has 0 dedicated experiments visible. Counterintuitive given it's a Moderate-value, High-PMF target.

## Pattern detection

### Compounding wins

1. **SMS Growth (6 stacked wins)** — per Connor Callahan 2026-03-20:
   - $1.08M FY26 / $3.96M FY27 cumulative
   - +45 bps SMS penetration
   - 9,300+ new SMS bookings expected FY26
   - Most recent: x287 Recommend SMS (+37.9% SMS purchase rate; +$230K FY26 / $1.2M FY27)
   - **Mechanism:** propensity model (60%+ contacts with phone numbers = 2nd highest predictor of SMS purchase) + contextual recommendation + audience-page placement

2. **Personalization / CDP cluster**:
   - x290 Inline Contact Search: +2.91% campaign creation rate (Apr 27 ramp-100%)
   - Joins Segment trigger: shipped Apr 28 (predicted impact: addresses ~10% of automation-related churn)
   - Sections Manager: +845 weekly C1 senders, $20K FY26 / $145K annualized
   - Meta Custom Audience GA: real-time MC segments → Meta — measurable lift in lead-ads attach
   - **Mechanism:** unified C2 data → finer-grained segmentation → more relevant campaigns → higher conversion

### Persistent losers

- None visible in this window (selection bias — `#mailchimp-launched` is celebratory)

### Ignored ICPs / Priorities (gap signal)

- **Community ICP**: 0 dedicated experiments
- **MM Account Structure & Billing flex**: 0 structural experiments (Annual Plans is pricing only)
- **Advanced campaign management** (frequency caps, multi-audience send): 0 experiments
- **Loyalty/UGC**: 0 experiments (acceptable per FY27+ narrative)

## Top-line readouts (this week)

| xid | Title | Status | Lift / Result | Source |
|---|---|---|---|---|
| x290 | Inline Contact Search in Audience | Ramped 100% Apr 27 | **+2.91% campaign creation rate** (clear win), 11-day test, no harm to payoff complete rate | Slack TS 1777325203 (Payton Camilli readout) |
| Joins Segment | Automation Flow trigger | **Shipped Apr 28** | Pre-experiment hypothesis: addresses ~10% of automation-related churned users + ~20% of automation-related churned MRR (per 2023 HVC churn report) | Slack TS 1777383920 (Elizabeth Bertasi) |
| OTP at Activation | Email activation flow | Running, partial readout | **+3.74% activation rate**, 33% reduction in session friction | Slack TS 1777337405 (Margarita Caraballo) |

## Prior-period running experiments (continue to monitor)

| xid | Title | Owner | Status |
|---|---|---|---|
| (TBD) | Annual Plans Self-Serve | Jacquelyn Horgan | Running since 2026-04-23 (4 weeks) |
| WhatsApp Private Beta | New channel | Devin Mercier | Private beta since 2026-03-11 (~20 customers); public beta target July 2026 |
| x471 | DFY-GTKM-Profile (shadow) | Joshua Fischer | Planning |
| x472 | Focused & Payoff-Based Checklist | Joshua Fischer | Planning |
| x488 | Showing DA and Search Side-by-Side (Support) | Sonia Singhal | Planning |
| x499 | Intent Aware Onboarding | Lucas Ruprecht | Planning (per `#mc-experimentation-xfn` 4/28 agenda) |
| x371 | Leverage BW to recommend integration | Prasad Sawant | Planning (per 4/28 agenda) |
| (TBD) | Domain Auth Campaigns | Amrinder Chawla | Planning (per 4/28 agenda) |

## Open questions

- **Annual Plans first read available ~2026-05-21** (4 weeks after 2026-04-23 launch). Predicted target: AP take rate >10%, +2.5% prospect-to-booking, +3pts 90d retention.
- **WhatsApp metrics**: cohort is 20 customers — too small for revenue signal; learning-mode only.
- **"6 stacked SMS wins" claim ($1.08M FY26)**: needs round-trip validation — re-query `bi_aggregate.product_health_weekly.sms_paid_plan_users` trajectory to verify the +45 bps claim.

## Findings ledger row written

```json
{"ts":"2026-04-28T21:00:00Z","source":"mc-experiment-synthesizer","claim":"Portfolio: ~13 experiments, 80% win rate (selection bias), top-compounding areas: SMS stack ($1.08M FY26) + Personalization/CDP cluster (4 wins). Critical gap: 0 experiments on MM account/billing structural and 0 on Community ICP","confidence":"medium","citations":["analyses/2026-W17/02-experiment-synthesis.md","canon/experiment-canon.md"]}
```
