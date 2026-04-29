# Executive Brief — 2026-W17

**Generated:** 2026-04-28 | **Owner:** Mailchimp Growth Strategist Agent | **For:** Deepak Prabhakaran

---

## SCQA

- **Situation:** Mailchimp is 9 months into FY26. Of 9 declared product priorities, **4 are shipped, 3 are in-flight, 2 are stuck**. The dominant compound winner is the **Personalization / CDP cluster** (4 stacked wins). The dominant validated revenue motion is the **SMS expansion stack** ($1.08M FY26 / $3.96M FY27 cumulative per Connor Callahan). Annualized MRR-at-risk = **~$76.5M** (active+passive); ~75% concentrated in 24+ tenure cohort.
- **Complication:** The current FY26 bet stack (top 5 levers, P50 sum = $18.2M) is **~$32M short of the $50M incremental target** within a 12-month horizon. The single largest unaddressed FY26 priority — **MM Account/Billing structural** (Priority 1 for MM Subscription/Community ICPs) — has **0 structural launches in 9 months** while Klaviyo and HubSpot already have parity. Separately, `sms_credit_purchases` is **declining 40% over 11 weeks**, threatening the cumulative SMS lift.
- **Question:** What three moves should Deepak champion this week to maximize the realistic path to $50M incremental?
- **Answer:** **(1) Double-down on the Personalization/CDP compound (highest score, 4 stacked wins). (2) Stand up the MM Account/Billing structural workstream — escalate for capacity/HC decision. (3) Diagnose the SMS credit-purchases decline this cycle so it doesn't quietly erode the strongest validated motion.**

---

## Top 3 Recommendations (with falsifiable predictions per G14)

### #1 — Double-down on the Personalization / CDP compound — **Commit**

- **Mechanism (named):** Each new behavioral-trigger primitive (e.g., "Joins Segment") makes existing automations more relevant to existing C2 data, lifting campaign creation rate (+2.91% per x290) AND reducing automation-driven churn (~10% of HVC churners per 2023 report). Compounded across 5-10 new primitives over 9 months → mid-single-digit % retention lift on the highest-MRR cohorts.
- **Pillars:** P1 Revenue=H, P2 Strategy=H, P3 Customer-problem=H, P4 Evidence=H, P5 Execution=H, P8 Compounding=H. Six H pillars — strongest evidence base in the portfolio.
- **ICP:** All 3 priority ICPs.
- **Predicted metric movement (G14):**
  - Metric: `email_creates` (per `bi_aggregate.product_health_weekly`)
  - Baseline: ~1.6M weekly creates
  - Predicted delta: **+3% to +5% on email_creates per active C1**
  - Window: 56 days (graded 2026-06-23)
  - Graded against: `queries/31-email-creates.sql`
- **Confidence:** **High** (named uncertainty: saturation risk on the 5th-10th primitive)
- **What would change my mind:** Next 2 personalization experiments come in neutral/negative; or Klaviyo ships step-function CDP advance.
- **Pre-mortem:** Saturation; capacity drain on Segmentation+CDP team; adverse selection (HVCs only).
- **Recommended next step:** Have Frank Persico (Segmentation EM) + Payton Camilli (Audience PM) propose the next 2 personalization experiments by **2026-05-12**. Push for behavioral pixel-trigger primitives + Gmail-activity sync.

### #2 — Stand up an MM Account/Billing structural workstream — **Conditional Commit**

- **Mechanism (named):** Multi-entity + parent-child + SSO + ACH/wire + contract price-lock removes structural blockers that today push MM customers ($5M-$10M revenue) toward Klaviyo or HubSpot. Closing this gap converts a fraction of MM-eligible MC users who today churn or downgrade due to operational-fit failures.
- **Pillars:** P2 Strategy=H, P3 Customer-problem=H, P8 Compounding=H. Three H pillars but **G4 capacity=HIGH (escalate)** — needs Deepak/SLT decision before HC commitment.
- **ICP:** Subscription MM (primary), Community Small/LMM (secondary).
- **Predicted metric movement (G14):**
  - Metric: `is_high_value=TRUE` Premium-tier weekly bookings (proxy for MM)
  - Baseline: ~59 Premium-tier bookings/week (week 4/19)
  - Predicted delta: **+20% to +35% within 12 months of structural billing infra landing**
  - Window: 365 days (graded 2027-04-28 — long horizon)
  - Graded against: `queries/14-bookings-by-tier.sql`
- **Confidence:** **Medium** (named uncertainty: Build-vs-Buy decision unanswered; no win/loss data validating the customer-need hypothesis)
- **What would change my mind:** Win/loss interviews show MM customers churn for OTHER reasons (e.g., feature gaps, not billing infra); or Klaviyo/HubSpot reduce MM-tier price aggressively.
- **Pre-mortem:** Build vs buy timing; no customer evidence yet; feature underutilization.
- **Recommended next step:** **2-week discovery (≤30 customer-conversation budget)** to validate the "MM customers churn over billing-infra" hypothesis BEFORE committing structural eng work. Owner: Jacquelyn Horgan + UXR partnership. Then re-evaluate.
- **🚨 ESCALATION:** Capacity decision (HC + reprioritization) requires Deepak/SLT call before commit.

### #3 — Diagnose the SMS Credit-Purchases decline (defensive) — **Conditional Commit (POL/Probe first)**

- **Mechanism (named):** A 40% decline in `sms_credit_purchases` over 11 weeks suggests one of: (a) saturation in current motion, (b) upstream funnel issue, (c) attribution change, or (d) deliberate ramp-down for IXP cutover. Each requires a different fix; ALL require diagnosis before doubling down on x287-style follow-on experiments.
- **Pillars:** P2 Strategy=H, P4 Evidence=H, P5 Execution=H, P6 Time-to-impact=H (fast).
- **ICP:** All — defensive across portfolio.
- **Predicted metric movement (G14):**
  - Metric: `sms_credit_purchases` (weekly)
  - Baseline: 645 (week 4/19)
  - Predicted delta: **return to >900/week within 4 weeks of intervention; OR flat-to-down if no intervention**
  - Window: 28 days (graded 2026-05-26)
  - Graded against: `queries/36-sms-metrics.sql`
- **Confidence:** **Medium-High** (named uncertainty: root cause unknown until diagnostic completes)
- **What would change my mind:** Discovering it's a measurement artifact, deliberate ramp-down for IXP cutover (per Jenn Reed 2026-04-27), or that Connor Callahan team is already on it.
- **Pre-mortem:** Wrong root-cause attribution; structural cause not fixable by SMS team; capacity diversion.
- **Recommended next step:** Connor Callahan + Ashish Prakash (DS) own a 2-week diagnostic. Output: root-cause attribution + go/no-go on a recovery experiment. Due **2026-05-12**.

---

## Prior-week prediction hit rate

**N/A — first run.** No prior predictions to grade. All subagent confidence weights initialized to neutral (no boost / no demote).

Rolling 12-week hit rate to be established over the next 12 cycles.

## New predictions written this run (3)

| recommendation_id | predicted_metric | predicted_delta | window | due |
|---|---|---|---|---|
| 2026-W17-rec-1 | email_creates | +3% to +5% | 56d | 2026-06-23 |
| 2026-W17-rec-2 | Premium-tier bookings (MM proxy) | +20% to +35% | 365d | 2027-04-28 |
| 2026-W17-rec-3 | sms_credit_purchases | return >900/wk OR flat-to-down | 28d | 2026-05-26 |

## Strategy-vs-Execution scorecard (this week)

| FY26 priority | Status | Evidence |
|---|---|---|
| P1 MM Account/Billing flex | **Stuck** (0 structural launches in 9 months) | Annual Plans is pricing/billing-term, not infra |
| P2 Channel Expansion (SMS, WhatsApp, social) | **Shipped+In-flight** | SMS: 6 stacked wins; WhatsApp private beta; social posts: not yet |
| P3 Integrations & Data Enablement | **Shipped** (4 wins) | Joins Segment, x290, Sections Manager, Meta CA GA |
| Ecomm P1 Personalization Depth | **Shipped** | Same 4 wins as P3; Shopify/BC/Woo parity gaps |
| Ecomm P2 Reporting & Attribution | **In-flight** | Analytics Agent V1 +6% creates; revenue attribution gap |
| Ecomm P3 Lead Ads | **Shipped (partial)** | Meta CA GA; Google Lead Ads pending |
| Loyalty / UGC | **Stuck (correctly)** | FY27+ exploration — OK |
| Advanced campaign management | **In-flight** | Frequency caps + multi-audience send not visible |
| AI Agents / DFY | **Shipped (1 measured)** | Project Alfred V1 |

## Open questions / escalations

- **🚨 Recommendation #2 escalation:** MM Account/Billing structural workstream needs HC/capacity decision. Surface to Deepak / SLT / Plans+PLC EMs.
- **PDF dashboard `new_booking_timing` % vs BigQuery numbers** disagree (logged in `contradictions.md`). Reconcile with Finance/DataEng next cycle.
- **% Churn Overview.xlsx** not parsed this cycle (openpyxl install required). Run `mc-doc-parser` next cycle.
- **External competitor research not run** — `mc-external-researcher` deferred. Schedule for next cycle.
- **Win/loss interview corpus (Gong/Heymarvin)** not piped — would dramatically tighten Recommendation #2 confidence.
- **`bi_finance.new_bookings_targets` / `paid_users_targets` not joined** — Growth Tree current run-rate estimate uses heuristics; should be exact.
- **Community ICP** has 0 dedicated experiments in 9 months despite highest MC penetration index (370 vs 3.2% baseline). Worth proposing in next cycle.

---

## Next-cycle priorities for the Strategist Agent

1. Grade the SMS-decline diagnostic prediction (window: 28 days)
2. Read first Annual Plans experiment results (~2026-05-21)
3. Run `mc-external-researcher` for fresh competitor intel
4. Parse `% Churn Overview.xlsx` to cross-validate cohort numbers
5. Re-query `bi_finance.new_bookings_targets` to pin down current FY26 trajectory
6. Add a Community ICP-specific experiment review in next cycle

---

## Run metadata

- **Subagents invoked:** 11 (1 orchestrator + 4 ingestion + 5 diagnostic + 1 synthesis-tree + 1 ranker + 4 QC)
- **Self-eval score:** 22/25 (≥20 publish gate met)
- **Predictions graded:** 0 (first run)
- **New predictions written:** 3
- **Findings ledger rows added:** ~12
- **Contradictions logged:** 1
- **Escalation flags:** 1 (Recommendation #2 capacity decision)
