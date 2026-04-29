# Recommendations (Ranked) — 2026-W17

**Run timestamp:** 2026-04-28
**Source inputs:** Growth Tree (06), Strategy Reconciler (01), Experiment Synthesizer (02), Churn Diagnostic (03), GTM Levers (04), Competitive Context (05)

## Top 3 (Commit / Conditional Commit)

---

### Recommendation #1 — Double-down on the Personalization / CDP compound — **Commit**

**Why this lever, not another:** It's the strongest *pattern of evidence* in the entire portfolio: 4 stacked wins (x290 Inline Search, Joins Segment trigger, Sections Manager, Meta Custom Audience GA) all at the CDP + Segmentation + Behavioral-trigger layer. P50 delta = $4.9M (highest score in Growth Tree, score 6.4).

**Gates:**
- G1 Strategy fit: **PASS** — maps to FY26 P3 (Integrations & Data Enablement) for MM and to P1 (Personalization Depth) for Ecomm
- G2 Evidence: **STRONG** — 4 concluded clear-wins, latest (x290) +2.91% campaign creation rate, Slack TS 1777325203
- G3 ICP fit: **PASS** — addresses all 3 priority ICPs (cross-cutting capability)
- G4 Capacity: **MEDIUM** — would extend the Audience/CDP team's roadmap; some risk of displacing other Audience work
- G5 Reversibility: **LOW** — experiment-first; each new behavioral trigger is independently shippable

**Pillars:**
- P1 Revenue: **H** — $5M-$10M realistic across full compound (Joins Segment alone closes ~10% of automation-driven churn per 2023 HVC churn report)
- P2 Strategy: **H** — direct match to FY26 P3 with multiple wins underway
- P3 Customer-problem severity: **H** — segments with worst MRR churn (Standard tier $32M annualized, 24+ tenure $57M) are most reachable via behavioral triggers
- P4 Evidence quality: **H** — 4 stacked wins, all with measured lift
- P5 Execution feasibility: **H** — team has shipped 4 things already
- P6 Time to impact: **M** — 9-12 months for full compound
- P7 Differentiation: **M** — Klaviyo has Shopify-native CDP; we're at parity, not ahead
- P8 Compounding: **H** — each new trigger compounds with prior (the namesake)
- P9 Reversibility: **H** — experiment-first

**Named mechanism:**
> Each new behavioral-trigger primitive (e.g., "Joins Segment") makes existing automations more relevant to existing C2 data, which lifts campaign creation rate (+2.91% per x290) AND reduces automation-driven churn (~10% of HVC churners have automation-related drivers per 2023 report). Compounded across 5-10 new primitives over 9 months → mid-single-digit % retention lift on the highest-MRR cohorts.

**ICP fit:** All three priority ICPs benefit (Subscription MM via segmentation depth, Community Small/LMM via behavioral re-engagement on registrants, Ecomm via Shopify+CDP product-data activation).

**Predicted metric movement (G14):**
- predicted_metric: `email_creates` (per `bi_aggregate.product_health_weekly`)
- predicted_baseline: weekly avg ~1.6M creates (trailing 13w)
- predicted_delta: +3% to +5% on `email_creates per active C1`
- predicted_window_days: 56 (8 weeks — long enough for next wave of personalization features to ship + ramp)
- graded_against: `queries/31-email-creates.sql`

**What would change my mind:**
- If the next 2 personalization experiments (after Joins Segment) come in neutral/negative
- If a competitor (especially Klaviyo) ships a step-function CDP advance that makes our trajectory feel commodity
- If the Segmentation team's bandwidth is fully consumed by Joins-Segment follow-on operational work

**Pre-mortem (3 reasons this fails):**
1. **Saturation** — we've already pulled the high-leverage levers; the 5th-10th personalization primitive yields diminishing returns
2. **Capacity drain** — Joins Segment + x290 follow-up + new triggers all hitting Segmentation+CDP teams simultaneously creates an oncall load that slows everything
3. **Adverse selection** — only HVC users adopt the new triggers; SMB users don't notice; lift comes from already-engaged customers, not the median

**Slack anchors:** TS 1777383920 (Joins Segment), TS 1777325203 (x290 readout), TS 1774972805 (Sections Manager), TS 1776776408 (Meta Custom Audience)

**Recommended next step:** Have Frank Persico (Segmentation EM) + Payton Camilli (Audience PM) propose the next 2 personalization experiments by 2026-05-12. Specifically push for: (a) behavioral pixel-trigger primitives, (b) Gmail-activity sync as a P3 priority lever.

**Escalation flags:** None.

---

### Recommendation #2 — Stand up an MM Account/Billing structural workstream — **Conditional Commit**

**Why this lever, not another:** It's FY26 Priority 1 for MM Subscription/Community ICPs with **zero structural launches in 9 months** (per Strategy Reconciler 01-* file). The MM ICP represents ~$10-15M realistic delta. Klaviyo and HubSpot already have parity (per FY26 narrative explicit citation). Every week we delay widens the parity gap.

**Gates:**
- G1 Strategy fit: **PASS** — explicit FY26 P1 for MM Subscription + Community
- G2 Evidence: **MODERATE** — Annual Plans is showing the team can ship pricing/billing-term experiments; structural billing infra is unproven internally
- G3 ICP fit: **PASS** — directly serves Subscription MM (high value, moderate PMF) and Community (moderate value, high PMF)
- G4 Capacity: **HIGH (escalate)** — likely requires HC investment or significant reprioritization. **ESCALATE** for Deepak / SLT decision.
- G5 Reversibility: **MEDIUM-HIGH** — architectural investment; commit-once-then-iterate

**Pillars:**
- P1 Revenue: **M** — $5M-$15M long-tail; not bookable in FY26
- P2 Strategy: **H** — explicit FY26 P1; the gap is the most-cited unaddressed priority
- P3 Customer-problem severity: **H** — competitive-parity signal: Klaviyo + HubSpot serve MM today, we're losing accounts on this dimension (anecdotal — needs win/loss data)
- P4 Evidence quality: **L** — claim relies on FY26 narrative + competitive narrative, NOT a concluded internal experiment
- P5 Execution feasibility: **M** — Plans/PLC team just shipped Annual Plans + Place of Supply tax; capacity in adjacent space exists but structural billing is a different scope
- P6 Time to impact: **L** — 12-18 months
- P7 Differentiation: **M** — catches up to competitor parity, doesn't differentiate
- P8 Compounding: **H** — once landed, unlocks MM-tier upsell + cross-Intuit bundling (FY27+)
- P9 Reversibility: **L** — billing infra changes are hard to roll back

**Named mechanism:**
> Multi-entity + parent-child + SSO + ACH/wire + contract-with-price-lock removes the structural blockers that today force MM customers to choose Klaviyo or HubSpot at the $5M-$10M revenue ceiling. Closing this gap converts a fraction of the ~10% of MM-eligible MC users who today churn or downgrade because of operational-fit failures (estimate, needs win-loss validation).

**ICP fit:** Subscription MM (primary), Community Small/LMM (secondary).

**Predicted metric movement (G14):**
- predicted_metric: `is_high_value=TRUE bookings_users` (Premium tier proxy for MM)
- predicted_baseline: ~52 Premium users/week + ~7 Premium-Annual = ~59/week (week 4/19)
- predicted_delta: +20% to +35% on Premium-tier weekly bookings within 12 months of structural billing infra landing
- predicted_window_days: 365 (long horizon — this is a structural bet)
- graded_against: `queries/14-bookings-by-tier.sql`

**What would change my mind:**
- Win/loss data (when piped) shows MM customers churn for reasons OTHER than billing infrastructure (e.g., feature gaps in agentic AI)
- Klaviyo or HubSpot meaningfully reduces MM-tier price/feature gap, making MC the value option
- Plans/PLC capacity is needed for higher-priority P&L work

**Pre-mortem (3 reasons this fails):**
1. **Build vs buy** — building multi-entity from scratch takes 18 months; by then competitors lap us. Should evaluate buying or partnering (Salesforce-style) for some pieces.
2. **No customer evidence** — assumption that MM customers churn over billing infra; without Gong/Heymarvin transcripts, this is hypothesis, not validated need.
3. **Feature underutilization** — Klaviyo's MM customers reportedly use only 30-40% of advanced features; building expensive structural infra that customers don't use is the worst outcome.

**Slack anchors:** TS 1776958294 (Annual Plans launch — adjacent work proves PLC team capacity), FY26 narrative (canon/fy26-strategy.md)

**Recommended next step:** Run a 2-week discovery (≤30 customer-conversation budget) to validate the "MM customers churn over billing-infra" hypothesis BEFORE committing structural eng work. Owner suggestion: Jacquelyn Horgan (Plans PM) + UXR partnership.

**Escalation flags:** ⚠️ **G4 capacity HIGH** — requires HC or major reprioritization. **ESCALATE** to Deepak / SLT for explicit decision before commit.

---

### Recommendation #3 — Diagnose the SMS Credit-Purchases decline (was #4 in Growth Tree but high urgency) — **Conditional Commit (POL/Probe first)**

**Why this lever, not another:** SMS expansion is the most-proven motion ($1.08M FY26 / $3.96M FY27 cumulative wins per Connor Callahan). BUT `bi_aggregate.product_health_weekly.sms_credit_purchases` is **declining 40% over 11 weeks** (week 2/8: 1,126 → week 4/19: 645). If unaddressed, this could erode the cumulative lift. It's a quiet metric drift that the org is not currently focused on.

**Gates:**
- G1 Strategy fit: **PASS** — FY26 P2 Channel Expansion + Expansion-sales motion
- G2 Evidence: **MODERATE** — 11-week BigQuery trend is clear; cause is not yet diagnosed (could be saturation, attribution change, or upstream funnel issue)
- G3 ICP fit: **PASS-PARITY** — SMS serves all ICPs
- G4 Capacity: **LOW** — diagnostic work, not new build
- G5 Reversibility: **LOW** — diagnostic-only; no commitment

**Pillars:**
- P1 Revenue: **M** — currently a defensive recommendation (preserve $4.5M P50 in stack); not net-new
- P2 Strategy: **H** — protects FY26 P2 lever
- P3 Customer-problem severity: **M** — needs investigation; could be customer-driven or platform-driven
- P4 Evidence quality: **H** — BigQuery trend is unambiguous
- P5 Execution feasibility: **H** — SMS Growth team (Connor Callahan) has capacity for diagnostic work
- P6 Time to impact: **H (fast)** — 2-week diagnostic
- P7 Differentiation: **M** — SMS is parity, not differentiation
- P8 Compounding: **M** — protects existing compound
- P9 Reversibility: **H** — diagnostic only

**Named mechanism:**
> A 40% decline in `sms_credit_purchases` over 11 weeks suggests one of: (a) saturation in current credit-purchase motion (we've converted the easy users), (b) upstream funnel issue (fewer Standard+Premium users on the audience-page where x287 fires), (c) attribution change (SMS purchases moved to a different metric / event), (d) deliberate slowdown for IXP cutover. Each of these requires a different fix, but ALL require diagnosis before doubling down on x287-style follow-on experiments.

**ICP fit:** All — defensive across portfolio.

**Predicted metric movement (G14):**
- predicted_metric: `sms_credit_purchases` (weekly)
- predicted_baseline: 645 (week 4/19)
- predicted_delta: diagnostic identified by 2026-05-19; if root-caused and addressed, return to >900/week within 4 weeks of intervention; if NOT root-caused, stay flat or decline further
- predicted_window_days: 28
- graded_against: `queries/36-sms-metrics.sql`

**What would change my mind:**
- Discovering that the decline is a measurement artifact (e.g., metric definition change in `product_health_weekly`)
- Discovering it's a deliberate ramp-down for IXP cutover (per `#mc-experimentation-xfn` 2026-04-27 Jenn Reed post: "All running experiments in Optimizely must be ramped down by Monday, June 15")
- Connor Callahan team already on it (would deduplicate effort)

**Pre-mortem (3 reasons this fails):**
1. **Wrong root cause attributed** — diagnostic concludes "saturation" when it's actually attribution change; we accept saturation and miss the real fix
2. **No fix possible** — root cause is structural (e.g., declining `is_high_value=TRUE` paid base) and not addressable through SMS-team levers alone
3. **Capacity diversion** — Connor Callahan team is already working on SMS standalone international rollout; diagnosing pulls focus

**Slack anchors:** TS 1774008120 (Connor x287 readout), `#mc-experimentation-xfn` 2026-04-27 (IXP cutover announcement, Jenn Reed)

**Recommended next step:** Connor Callahan + Ashish Prakash (DS) own a 2-week diagnostic. Output: root-cause attribution + go/no-go on a recovery experiment. Due 2026-05-12.

**Escalation flags:** None.

---

## Considered but not in top 3

### Annual Plans — push for AP take rate >10% in first 4-week read
- Already #1 P50 contributor in Growth Tree but **timing constraint**: first read 2026-05-21. Cannot recommend a SECOND action before reading the first one. Defer to next cycle once we have the data.

### DFY Agentic AI / Analytics Agent expansion (Growth Tree #5)
- Score 3.3 (lower than top 3). Plus **G10 escalation flag** — touches Deepak's surface; do not auto-recommend changes.

### Legacy Plan billing-failure recovery (Growth Tree candidate-new lever)
- Score $3.2M P50; quiet $13M annualized passive churn. **Worth proposing in next cycle** once we have explicit ownership clarity (currently no FY26 owner).

### MM Premium Tier (above current Premium)
- Dependent on Recommendation #2 landing first. Would propose in Q3-Q4 once structural billing in flight.

### Cross-Intuit referral / QBO bundle (FY27+ exploration)
- Out of scope for FY26 Commit. Note in `program.md` for monitoring.

### International SMS standalone
- Strong fit but tied to MM Account/Billing flex (#2) AND SMS diagnostic (#3). Defer.

---

## Predictions written to predictions-ledger.jsonl

```json
{"run_ts":"2026-04-28T21:00:00Z","run_yyyy_ww":"2026-W17","recommendation_id":"2026-W17-rec-1","title":"Personalization/CDP compound","predicted_metric":"email_creates","predicted_baseline":1635591,"predicted_delta":"+3% to +5% on email_creates per active C1","predicted_window_days":56,"predicted_due_at":"2026-06-23T21:00:00Z","graded_against":"31-email-creates","subagent_attribution":"mc-recommendation-ranker","actual_delta":null,"graded_at":null,"hit":null}
{"run_ts":"2026-04-28T21:00:00Z","run_yyyy_ww":"2026-W17","recommendation_id":"2026-W17-rec-2","title":"MM Account/Billing structural","predicted_metric":"is_high_value bookings (Premium tier proxy)","predicted_baseline":59,"predicted_delta":"+20% to +35% on Premium-tier weekly bookings","predicted_window_days":365,"predicted_due_at":"2027-04-28T21:00:00Z","graded_against":"14-bookings-by-tier","subagent_attribution":"mc-recommendation-ranker","actual_delta":null,"graded_at":null,"hit":null}
{"run_ts":"2026-04-28T21:00:00Z","run_yyyy_ww":"2026-W17","recommendation_id":"2026-W17-rec-3","title":"SMS credit-purchases decline diagnostic","predicted_metric":"sms_credit_purchases","predicted_baseline":645,"predicted_delta":"return to >900/week within 4 weeks of intervention; or flat-to-down if no intervention","predicted_window_days":28,"predicted_due_at":"2026-05-26T21:00:00Z","graded_against":"36-sms-metrics","subagent_attribution":"mc-recommendation-ranker","actual_delta":null,"graded_at":null,"hit":null}
```

## Findings ledger row written

```json
{"ts":"2026-04-28T21:00:00Z","source":"mc-recommendation-ranker","claim":"Top 3 recs (with G14 predictions): 1) Personalization/CDP compound (predicted +3-5% email_creates by 2026-06-23); 2) MM Account/Billing structural (escalation flag - HC/capacity decision); 3) SMS credit-purchases decline diagnostic (2-wk POL).","confidence":"medium","citations":["analyses/2026-W17/07-recommendations.md","predictions-ledger.jsonl"]}
```
