# Recommendations (Ranked by Ownership Tier) — 2026-W17

**Run timestamp:** 2026-04-29 (rewritten with OWN/INFLUENCE/ESCALATE ownership lens)
**Source inputs:** RA opportunities (09), Growth Tree (06), Strategy Reconciler (01), Experiment Synthesizer (02), Churn Diagnostic (03), GTM Levers (04), Competitive Context (05)

## Ownership-tier summary

| Tier | Count shown | P50 sum | % of $50M |
|---|---|---|---|
| **OWN** (Deepak commissions directly) | 3 Commit + 2 Conditional | ~$8.4M | 17% |
| **INFLUENCE** (Deepak co-sponsors with partner PMs) | 2 | ~$9.4M | 19% |
| **ESCALATE** (SLT decisions) | 2 | ~$4.4M | 9% |
| **Stack total (top recs)** | | **~$22M** | **44%** |

> **R&A alone cannot close $50M.** The realistic stack combining Deepak's OWN work + INFLUENCE partners + ESCALATE asks reaches ~44% of the target. The remaining ~56% is either (a) beyond 12-month horizon or (b) requires new levers not yet in motion (see Growth Tree § Candidate NEW levers).

---

## PART 1 — OWN tier (Deepak commissions directly) [3 Commit + 2 Conditional]

### Recommendation #1 — **Scale Analytics Agent V1 → V2 full paid base** [OWN, Commit]

**Mechanism:** V1 measured +6% email campaigns/user lift with >99% significance in a 50K cohort (per Stephen Yu 2026-03-13, Slack TS 1772468019). Scaling to ~993K paid users — with honest lift attenuation — preserves 25% of measured lift = **~$4.0M P50 annualized**. Mechanism: AI-native conversational analytics → more campaigns sent → more retained engagement → lower churn + higher ARPU.

**Gates:** G1 Strategy=PASS (FY26 DFY Agentic P1), G2 Evidence=STRONG (1 concluded exp), G3 ICP=PASS (all 3), G4 Capacity=MEDIUM (1-2 HC), G5 Reversibility=LOW (experiment-first ramp)

**Pillars (≥1 High with named mechanism per G5):** P1 Revenue=H ($4.0M P50), P2 Strategy=H (FY26 P1 Agentic), P4 Evidence=H (>99% sig), P5 Execution=H (team shipped V1), P8 Compounding=H (unlocks B, F, G).

**Predicted metric movement (G14):**
- Metric: `email_creates per active C1` 
- Baseline: ~0.85 creates/active-user (trailing 13w)
- Delta: **+3% to +6% creates/active-user once V2 reaches ≥500K users**
- Window: 180 days
- Graded against: `queries/31-email-creates.sql` + new normalization query

**Business case detail:** realistic P50 $4.0M / P90 $9.0M; probability 0.65; time to impact 9 months.

**Capacity ask:** 1-2 HC on AI Agent eng + inference costs budget
**Partner dependencies:** SMS Growth (data pipe), AI Science, DS, TPM
**What would change my mind:** V2 beta cohort shows <1% lift at 200K scale (saturation ceiling hit early), or Klaviyo Breeze ships parity-level feature before our GA.
**Pre-mortem:** Lift attenuation >expected; infra cost negative at scale; competitor response erases moat.
**Recommended next step:** Lock V2 ramp plan with Stephen Yu (AI Agent PM) + Kuntal Naphade (Eng) by **2026-05-12**. Define the 200K → 500K → full-base ramp gates with attenuation thresholds.

---

### Recommendation #2 — **Productize Churn-Prediction insights in Analytics Agent** [OWN, Commit]

**Mechanism:** Annualized MRR-at-risk = $76.5M (per 03-churn-diagnostic). 75% concentrated in 24+ tenure and Standard-tier. Surfacing propensity-model outputs inside Analytics Agent (for C1s AND CSMs) enables intervention at onset of churn signal instead of after billing failure. Conservative recovery assumption: 15% of actually-lost MRR (industry benchmark) = **~$5.5M P50 annualized**.

**Gates:** G1=PASS (FY26 $14.9M churn reduction target), G2=MODERATE (cohort data strong, no end-to-end exp yet), G3=PASS-PARITY, G4=HIGH (2-3 HC + DS), G5=LOW (experiment-first)

**Pillars:** P1 Revenue=H ($5.5M P50), P2 Strategy=H (direct FY26 match), P3 Customer-problem=H ($76.5M at-risk), P4 Evidence=M (no concluded exp in this combination), P5 Execution=M (DS precedent via SMS propensity).

**Predicted metric movement (G14):**
- Metric: **Active churn MRR** (from `bi_aggregate.churn_daily.active_churn_risk_orders`)
- Baseline: ~$26.5M annualized
- Delta: **-5% to -10% on active churn MRR within 12 months**
- Window: 365 days
- Graded against: `queries/22-active-churn-mrr.sql`

**Business case:** P50 $5.5M / P90 $11M; probability 0.5; time to impact 6-9 months. **Highest-score OWN bet** (4.4).

**Capacity ask:** 2-3 HC AI Agent eng + 1 DS allocation
**Partner dependencies:** Data Science (Ashish Prakash, Jeremy Diaz, Himanshu Dubey); ⚠️ **Gainsight/CSM integration is the 2x leverage multiplier — currently a coverage gap.**
**What would change my mind:** Propensity-model precision <60% in pilot (false-positive avalanche kills CSM adoption); OR Gainsight integration proves impossible in 12 months (cap at C1-self-serve only).
**Pre-mortem:** Model precision problem; intervention fails (identifying at-risk is easy, recommending right action is hard); CSM pipe never lands.
**Recommended next step:** 2-week scoping sprint with Ashish Prakash (DS) to validate model precision on HVC cohort. Then decide: full-launch vs. HVC-only POL. Due **2026-05-19**.

---

### Recommendation #3 — **Annual Plans reporting & attribution accelerator** [OWN, Commit]

**Mechanism:** Annual Plans experiment live 2026-04-23; first read ~2026-05-21. Predicted FY27 incremental $1.3M-$3.9M per launch post. R&A lacks first-class AP reporting. Mechanism: ship AP dashboard in <4 weeks → Plans team reads faster → iterates twice in 12-week window vs. once → **pull 20-30% of FY27 impact into FY26**.

**Gates:** G1=PASS (unblocks Plans bet), G2=STRONG (live experiment), G3=PASS (all 3 ICPs via trial-entry), G4=LOW (1 eng + 1 analyst, 2-week sprint), G5=LOW

**Pillars:** P1 Revenue=M ($0.55M in-year acceleration), P2 Strategy=H (unblocks Plans), P3 Customer-problem=M (PM decision speed), P4 Evidence=STRONG, P5 Execution=H, P6 Time-to-impact=**H** (fastest win).

**Predicted metric movement (G14):**
- Metric: **time from experiment start to in-brief readout**
- Baseline: ~28 days historically
- Delta: **<14 days for AP experiment readouts**
- Window: 42 days
- Graded against: qualitative audit + Plans PM confirmation

**Business case:** P50 $0.55M / P90 $1.0M; probability 0.75; time to impact 4-6 weeks. **Highest-speed, lowest-capacity-cost OWN bet.**

**Capacity ask:** 1 R&A Eng + 1 data analyst; 2-week sprint
**Partner dependencies:** Plans PM (Jacquelyn Horgan), FinOps, DS (Ethan Ham), Finance
**Recommended next step:** Kick off this week. Request experiment-design doc from Jacquelyn Horgan by **2026-05-05**; target dashboard GA by **2026-05-19** (ahead of first read).

---

### Recommendation #4 — **Ecomm-specific reporting (GMV, ROI, per-product attribution)** [OWN, Conditional Commit]

**Mechanism:** Digital Sales-based ICP (21% of user base, 25% of revenue) needs GMV + ROI + per-product attribution to justify MC spend. Currently parity gap with Klaviyo. Mechanism: Ecomm customers with visible ROI retain longer + upgrade to Premium at higher rates.

**Gates:** G1=PASS (FY26 Ecomm P2), G2=MODERATE (narrative + competitive, no internal exp), G3=PASS (Ecomm ICP), G4=MEDIUM, G5=MEDIUM

**Conditional on:** Audience/CDP team (Payton Camilli) committing to Shopify product-catalog data activation in H1 FY26. Without that upstream commit, **defer to FY27**.

**Predicted metric movement (G14):**
- Metric: **Connected-ecomm user 6mo churn rate**
- Baseline: 31%
- Delta: **-1.5pt to -3pt** once ROI dashboards ship + ≥20% of ECU base adopts
- Window: 365 days
- Graded against: `queries/40-cohort-churn-by-package.sql` with ecomm_status filter

**Business case:** P50 $2.5M / P90 $5M; probability 0.5; time to impact 9-12 months.

**Recommended next step:** Formalize the dependency ask with Payton Camilli this month. If no upstream commit by **2026-05-26**, defer to FY27 and redirect capacity to Rec #7 (Predictive upsell).

---

### Recommendation #5 — **Top-3 Reporting UX VOC fixes (Export fields, Data Accuracy, A/B export)** [OWN, Conditional Commit (POL-first)]

**Mechanism:** Per `last-stretch-voc-analyzer` (existing agent), top-3 R&A VOC themes recur weekly. HVC-concentrated ($6,664 MRR World Central Kitchen; $3,488 MRR HC Brands flagged). Mechanism: fix → unblock HVC workflow → reduce HVC churn signal → preserve high-ARPU revenue.

**Gates:** G1=PASS, G2=STRONG (VOC data), G3=PASS-PARITY (HVC-weighted, skews to all-ICP HVCs), G4=LOW (1 Eng + 1 Designer), G5=LOW

**POL/Probe first:** Before committing full build, run a 2-week diagnostic — is R&A VOC actually causing HVC churn, or just co-occurring? Cross-reference VOC-user list with churn-risk cohort from `churn_daily`.

**Predicted metric movement (G14):**
- Metric: **HVC-weighted R&A VOC volume (per last-stretch-voc-analyzer)**
- Baseline: 50-120 R&A-themed VOCs/week
- Delta: **-30% within 12 weeks of fix ship**
- Window: 120 days
- Graded against: last-stretch-voc-analyzer output (integration required — coverage gap Tier 3.1)

**Business case:** P50 $0.75M / P90 $2M; probability 0.7; time to impact 3-6 months.

**Recommended next step:** Deepak + 1 Eng scope the POL by **2026-05-12**. Cross-reference VOC-user list with `bi_aggregate.churn_daily` cohort to validate causation.

---

### Considered but not in top 5 (OWN tier)

- **F — Predictive upsell agent in Analytics Agent** — P50 $3.4M × 0.4 probability. Good upside but 9-12 months and depends on Plans upgrade-flow integration. Defer to next cycle unless Rec #4 is cancelled.
- **G — "Why am I losing customers" DFY agent** — P50 $3.0M × 0.4 probability. Highest differentiation vs Klaviyo/HubSpot. Depends on Rec #2 landing first. Defer to Q3 FY26 cycle.
- **H — MM multi-entity reporting** — dependent on ESCALATE #2 (MM Account/Billing). DEFER.

---

## PART 2 — INFLUENCE tier (Deepak co-sponsors; partner PM commissions)

### Recommendation #6 — **Personalization / CDP compound: next 2 primitives** [INFLUENCE, Commit]

**Partner:** Payton Camilli (Audience PM) + Frank Persico (Segmentation EM).

**Mechanism:** 4 stacked wins in this area (x290 Inline Search, Joins Segment, Sections Manager, Meta Custom Audience). Next primitives (behavioral pixel-triggers, Gmail-activity sync) compound. R&A consumes the output for Analytics Agent V2 (Rec #1).

**Business case:** P50 $4.9M × probability 0.65 = $3.2M expected contribution. (Per Growth Tree.)

**R&A role:** Analytics Agent V2 surfaces the insights generated by these new primitives. Co-sponsor, don't lead.

**Predicted metric movement (G14):** (same as prior week)
- Metric: `email_creates`
- Delta: +3% to +5%
- Window: 56 days

**Recommended next step:** Deepak joins Payton + Frank's roadmap sync to ensure Analytics Agent V2 consumes the new primitives within the 9-month window for Rec #1.

---

### Recommendation #7 — **SMS credit-purchases decline diagnostic** [INFLUENCE, POL/Probe]

**Partner:** Connor Callahan (SMS Growth PM) + Ashish Prakash (DS).

**Mechanism:** `sms_credit_purchases` declining 42.7% over 11 weeks (per 04-gtm-levers). Protects the $4.5M P50 on SMS expansion lever. R&A provides the diagnostic dashboard.

**Business case:** Defensive. Preserves $4.5M P50 rather than adding.

**Predicted metric movement (G14):**
- Metric: `sms_credit_purchases` (weekly)
- Baseline: 645 (week 4/19)
- Delta: **>900/wk within 4 weeks of intervention, OR flat-to-down**
- Window: 28 days
- Graded against: `queries/36-sms-metrics.sql`

**R&A role:** build a one-off diagnostic dashboard for Connor's team. 3-day effort.

**Recommended next step:** Connor Callahan + Ashish Prakash own diagnostic; Deepak sponsors R&A's dashboard support. Due **2026-05-12**.

---

## PART 3 — ESCALATE tier (SLT decisions required)

### Recommendation #8 — 🚨 **Stand up MM Account/Billing structural workstream** [ESCALATE]

**Partner:** Plans/PLC EM + SLT.

**Mechanism:** FY26 Priority 1 for MM Subscription/Community. **0 structural launches in 9 months** while Klaviyo + HubSpot have parity. Closing this gap converts MM customers who would otherwise churn to competitors at the $5M-$10M revenue ceiling.

**Business case:** P50 $4.0M × probability 0.4 = $1.6M expected; long horizon (12-18 months).

**R&A downstream:** enables Rec #9 (MM multi-entity reporting) — compound value.

**Capacity ask:** HC + eng headcount at Plans/PLC; **escalation to Deepak's SLT for strategic capacity reallocation.**

**Predicted metric movement (G14):**
- Metric: `is_high_value=TRUE` Premium-tier weekly bookings (MM proxy)
- Baseline: ~59/week (week 4/19)
- Delta: +20% to +35% within 12 months of infra landing
- Window: 365 days

**What would change my mind:** Win/loss interviews (gap) show MM customers churn for reasons OTHER than billing infra.

**Recommended next step:** 2-week discovery budget (≤30 customer-conversations) BEFORE committing structural eng. Owner: Jacquelyn Horgan + UXR partnership.

---

### Recommendation #9 — 🚨 **Gainsight / CSM integration for Churn-Prediction Agent (B)** [ESCALATE]

**Partner:** Customer Success leadership.

**Mechanism:** Rec #2 (Churn-Prediction Agent) has 2x leverage multiplier *if* CSMs can surface/act on predictions in their Gainsight workflow. Currently coverage gap (Tier 1.2 per `canon/coverage-gaps.md`).

**Business case:** Moves Rec #2 from P50 $5.5M to P50 $11M (the P90 case becomes realistic). Net uplift: $5.5M expected value IF integration lands.

**R&A role:** provides the insights; CS leadership must commit workflow integration.

**Recommended next step:** Deepak escalates to CS leadership (name in `canon/org-glossary.md` — to confirm); request joint scoping for H2 FY26.

---

## Predictions written to predictions-ledger.jsonl

The following predictions are being appended (see `predictions-ledger.jsonl`). All recommendations with measurable outcome predictions are tracked.

| rec_id | tier | title | metric | delta | window_days | due |
|---|---|---|---|---|---|---|
| 2026-W17-own-1 | OWN | Analytics Agent V2 scale-up | email_creates/active-C1 | +3% to +6% | 180 | 2026-10-26 |
| 2026-W17-own-2 | OWN | Churn-Prediction Agent | active_churn_mrr | -5% to -10% | 365 | 2027-04-29 |
| 2026-W17-own-3 | OWN | AP reporting accelerator | exp-to-readout time | <14 days | 42 | 2026-06-10 |
| 2026-W17-own-4 | OWN | Ecomm reporting | ECU 6mo churn rate | -1.5 to -3pt | 365 | 2027-04-29 |
| 2026-W17-own-5 | OWN | Top-3 VOC fixes | R&A VOC volume (HVC) | -30% | 120 | 2026-08-27 |
| 2026-W17-inf-6 | INFLUENCE | Personalization compound (prior) | email_creates | +3% to +5% | 56 | 2026-06-24 |
| 2026-W17-inf-7 | INFLUENCE | SMS diagnostic | sms_credit_purchases | >900/wk or flat | 28 | 2026-05-27 |
| 2026-W17-esc-8 | ESCALATE | MM Account/Billing structural | Premium-tier bookings | +20% to +35% | 365 | 2027-04-29 |

## Findings ledger row

```json
{"ts":"2026-04-29T21:00:00Z","source":"mc-recommendation-ranker","claim":"2026-W17 v2 with ownership tiering: 5 OWN recs (P50 $8.4M = 17% of $50M), 2 INFLUENCE (P50 $9.4M), 2 ESCALATE (P50 $4.4M). Headline OWN: (1) Analytics Agent V2 scale, (2) Churn-Prediction Agent, (3) AP reporting accelerator. Stack ~44% of $50M.","confidence":"medium","citations":["analyses/2026-W17/07-recommendations.md","analyses/2026-W17/09-ra-ai-opportunities.md","predictions-ledger.jsonl"]}
```
