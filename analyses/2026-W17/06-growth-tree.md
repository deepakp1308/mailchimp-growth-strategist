# Growth Tree → $50M Incremental — 2026-W17

**Run timestamp:** 2026-04-28
**Window:** trailing 13 weeks (2026-01-26 → 2026-04-26)
**Source data:** `bi_aggregate.product_health_weekly`, `bookings_weekly`, `churn_daily`

## The tree

```
Annualized Revenue
  = Avg Paid Users
    × ARPU (annualized)
    × (1 - annual churn rate)
    × (1 + net expansion rate)
```

## Current trajectory (steady state, trailing 13 weeks)

| Input | Value | Source |
|---|---|---|
| Avg Paid Users | ~993,000 (per Exec Overview Apr 19) | Tableau cross-check |
| Avg new bookings/week (users) | ~7,500 | bookings_weekly avg of 13 weeks |
| Avg new bookings/week ($) | ~$295K | bookings_weekly avg |
| Avg activations/week | ~41,400 (full weeks only) | product_health_weekly |
| sms_paid_plan_users (latest) | ~34,300 | product_health_weekly |
| Active weekly churn rate | 0.95% | Exec Overview dashboard |
| Passive weekly churn rate | 0.45% | Exec Overview dashboard |
| **Annualized active+passive MRR-at-risk** | **~$76.5M** | churn_daily cohorts |

**Estimated annualized revenue run-rate:** ~$650M-$1.1B (Intuit MC segment-level public reporting; MC product-only is ~$650M-$750M based on derived from churn-rate × MRR-at-risk math)

> The Growth Strategist agent should sharpen this estimate via direct MC P&L access (currently a gap — Finance MCP not piped).

## $50M target context

Assuming current run-rate ~$700M annualized:

- **$50M = ~7%** growth on annualized revenue
- Equivalent to:
  - Adding ~70K paid users (vs current ~993K base) — **+7% paid users**, OR
  - Increasing ARPU from $704/yr to $755/yr — **+7% ARPU**, OR
  - Reducing total churn $/yr from $76.5M to $26.5M — **−65% MRR-at-risk** (very aggressive), OR
  - Combination of above

## Single-lever sensitivity (1-at-a-time)

For each lever, assume all others held constant and compute the delta needed to add $50M annually.

| Lever | Current | Delta needed alone | % change | Realistic? |
|---|---|---|---|---|
| **Paid Users** | 993K | +71K users | +7% | Possible but requires 35K extra activations/year sustained |
| **ARPU (yearly)** | ~$704 (derived) | +$50 | +7% | Achievable via tier-mix shift (Annual Plans + MM acquisition) |
| **Active churn $-rate** | $26.5M/yr at risk → $14M lost (50% conv) | -$50M | -3.5x → impossible alone | Only as part of stack |
| **Passive churn $-rate** | $50M/yr at risk → $25M lost | -$50M | impossible alone | Combined w/ active possible |
| **Net expansion (SMS)** | $1.08M FY26 cumulative (per Connor) | +$48M | impossible alone | Long-term, multi-channel needed |
| **AP take rate** (post-Apr 23) | 3% baseline (current) → target >10% | take rate to >50% | not realistic | $1.3M-$3.9M FY27 max alone |
| **Activation rate** | currently moving via OTP +3.74% | additional +6% | needs OTP + onboarding overhaul | Possible w/ DFY agentic landing |
| **FT Rolloff rate** (current week) | 21% of $ bookings | needs +30% lift on conversion | aggressive | Annual Plans + MM tier may help |

## Pareto-ranked levers (top 5)

Score = `realistic_delta × probability × (12 / time_to_impact)`

### #1 — Annual Plans (combined acquisition + retention)
- **Realistic delta:** $1.3M-$3.9M FY27 (per launch announcement, Slack TS 1776958294)
- **Probability:** 0.6 (rate-card experiment, first read 2026-05-21 — 4 wk wait)
- **Time to impact:** 6 months
- **Score:** ~$3.9M × 0.6 × 2 = **4.7**
- **Mechanism:** lower opening price point + 14-day FT for Standard/Essentials → higher conversion + longer commitment lock-in → 90d retention lift
- **Backing experiment:** AP launch (live)
- **FY26 priorities matched:** Pricing/Packaging (implicit), MM acquisition (partial), Scaled acquisition

### #2 — MM Account/Billing Structural (THE GAP)
- **Realistic delta:** $5M-$15M annually (estimated from MM TAM × MC penetration potential lift; needs sharper estimate)
- **Probability:** 0.4 (currently 0 structural launches in 9 months — execution risk is HIGH)
- **Time to impact:** 12 months minimum
- **Score:** ~$10M × 0.4 × 1 = **4.0**
- **Mechanism:** multi-entity + parent-child + SSO + ACH/wire + contract price-lock → addresses the "$10M revenue" MM ceiling that Klaviyo + HubSpot currently capture
- **Backing experiment:** NONE (gap signal — see Strategy Reconciler)
- **FY26 priorities matched:** P1 MM Subscription/Community (the largest unaddressed priority)

### #3 — Personalization/CDP compound (Joins Segment + Pixel + GA + Gmail sync)
- **Realistic delta:** $5M-$10M (compound effect: x290 +2.91% campaign creation × 50K eligible users × $300 ARPU × retention lift)
- **Probability:** 0.65 (4 stacked wins in this area — the strongest compounding cluster)
- **Time to impact:** 9 months
- **Score:** ~$7.5M × 0.65 × 1.3 = **6.4** ⬆️ HIGHEST SCORE
- **Mechanism:** unified C2 profiles → behavior-triggered automations → +retention + +activation + +conversion across the full funnel
- **Backing experiments:** x290 (concluded clear-win), Joins Segment (just shipped), Sections Manager, Meta Custom Audience GA — 4 stacked wins
- **FY26 priorities matched:** P3 Integrations & Data Enablement, P1 Ecomm Personalization Depth

### #4 — SMS expansion (continue the proven motion)
- **Realistic delta:** $3.96M FY27 cumulative (per Connor) → likely $5M-$8M annualized as motion compounds
- **Probability:** 0.75 (6 stacked wins — the most proven motion)
- **Time to impact:** 6 months
- **Score:** ~$6M × 0.75 × 2 = **9.0** ⬆️⬆️ HIGHEST SCORE
- **Mechanism:** propensity model (60%+ contacts with phone numbers) + contextual recommendations + audience-page placement → SMS purchase rate +37.9% per x287
- **Caveat:** `sms_credit_purchases` declining 40% over 11 weeks; signals saturation in current motion. Need new growth vectors: SMS standalone, international, cross-channel orchestration
- **Backing experiments:** 6 stacked wins per Connor 2026-03-20
- **FY26 priorities matched:** P2 Channel Expansion (MM Subscription/Community)

### #5 — DFY Agentic AI / Analytics Agent expansion
- **Realistic delta:** $3M-$8M (Project Alfred showed +6% email creates per user at 50K; scaling to full base = significant productivity multiplier on base activity)
- **Probability:** 0.5 (single measured experiment — needs validation at scale)
- **Time to impact:** 9 months (V2 ramp)
- **Score:** ~$5M × 0.5 × 1.3 = **3.3**
- **Mechanism:** AI-native analytics + recommendations → reduce churn-risk customer requests from "weeks to build" to "instant" + drive more campaigns sent per user → more value realization → retention
- **Backing experiment:** Project Alfred V1 test (Stephen Yu 2026-03-13)
- **FY26 priorities matched:** Agentic AI / DFY (segment-agnostic P1)
- **Escalation flag:** ⚠️ Touches Analytics Agent GA scope — Deepak's surface — do not auto-recommend changes; surface for human decision.

## Stack scenario (top 5 combined)

P50 sum (probability × realistic):
- #1 AP: $3.9M × 0.6 = **$2.3M**
- #2 MM Account/Billing: $10M × 0.4 = **$4.0M**
- #3 Personalization/CDP: $7.5M × 0.65 = **$4.9M**
- #4 SMS expansion: $6M × 0.75 = **$4.5M**
- #5 DFY Agentic: $5M × 0.5 = **$2.5M**

**P50 sum = $18.2M**

**Vs $50M target: gap of $31.8M.**

The current FY26 bet stack does NOT close $50M alone. **Need to add candidate-new levers OR accept that $50M is a 18-24 month horizon, not 12.**

## Candidate NEW levers (not currently in motion)

| Lever | Realistic delta (annual) | Probability | Notes |
|---|---|---|---|
| **Legacy plan billing-failure recovery** | $3M-$6M | 0.7 | Per Churn Diagnostic: legacy_monthly cohort has $13M annualized passive churn; better dunning + payment-method update workflows could recover 25-50%. **Currently invisible in FY26 narrative** — quiet, high-leverage. |
| **MM Premium tier (above current Premium)** | $5M-$10M | 0.4 | New tier above current Premium with multi-entity + contracts + SSO. Would convert ~10% of current Premium users at 50%-100% premium price. Requires P1 structural work to land first. |
| **Pricing optimization on list-price** (not just AP discount) | $4M-$8M | 0.5 | Current Standard/Essentials list-prices unchanged in 2+ years; competitor Klaviyo went up 10% in 2026; HubSpot Hub-tier increase. Modest list-price increase + AP discount = net +ARPU. Risky on churn. |
| **Cross-Intuit referral / bundle (QBO ↔ MC)** | $5M-$15M | 0.3 | FY27+ in narrative; H1 FY26 clarification expected. Highest defensible-moat play but slow to land. |
| **International SMS short-codes / standalone** | $2M-$5M | 0.6 | Specifically called out in FY26 narrative P2 (MM Channel Expansion). 0 launches yet. Connor's Watchtower already monitoring — execution-ready. |
| **Loyalty / UGC partner (Yotpo/Loox-equivalent integration)** | $1M-$3M | 0.5 | FY27+ exploration; partner-led path could move faster than build. |

## Stack scenario WITH top 2 candidate new levers

Add: legacy billing-failure recovery ($4.5M × 0.7 = $3.2M) + MM Premium tier ($7.5M × 0.4 = $3.0M)

**Updated P50 sum = $18.2M + $6.2M = $24.4M**

Still ~$25M short of $50M. **Either**:
- Accept 18-24 month horizon and treat $50M as the 2-year target, OR
- Find aggressive new lever (e.g., consumption-based pricing, marketplace monetization, or major tier restructuring), OR
- Increase probability via execution intensity (capacity reallocation toward MM + Personalization compound).

## Headline recommendation hint (NOT a recommendation — for ranker)

The single highest-leverage move is to **double down on the Personalization/CDP compound** (Lever #3, score 6.4). It's the strongest pattern of evidence (4 stacked wins), addresses both retention (via Joins Segment, x290) and acquisition (via Meta CA → Lead Ads), and has the broadest ICP coverage (works for all 3 priority ICPs).

The single biggest **gap to close** is **MM Account/Billing structural** — it's an FY26 P1 with 0 structural launches in 9 months, and Klaviyo + HubSpot already have parity. Even at 0.4 probability, the realistic-delta of $10M makes this the second-highest-score lever.

## Findings ledger row written

```json
{"ts":"2026-04-28T21:00:00Z","source":"mc-growth-tree-50m","claim":"Top 3 levers (realistic-delta × probability): 1) Personalization/CDP compound P50 $4.9M, 2) SMS expansion P50 $4.5M, 3) MM Account/Billing structural P50 $4.0M. P50 stack of top 5 = $18.2M. Plus top-2 candidate new levers = $24.4M. Gap to $50M = ~$25M; suggests $50M is a 18-24 month horizon not 12.","confidence":"medium","citations":["analyses/2026-W17/06-growth-tree.md"]}
```
