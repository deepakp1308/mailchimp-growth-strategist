# Executive Brief — 2026-W17

**Generated:** 2026-04-29 (v2 with R&A + AI Agent ownership lens)
**Owner:** Mailchimp Growth Strategist Agent
**For:** Deepak Prabhakaran (PM, Reporting & Analytics + Analytics AI Agent)

---

## SCQA

- **Situation:** Mailchimp is 9 months into FY26 with $76.5M annualized MRR-at-risk and a $50M incremental-growth target on the table. Of the 9 declared FY26 priorities, 4 are shipped, 3 in-flight, 2 stuck. Deepak owns the **R&A + Analytics AI Agent** surface, which has one measured win (Analytics Agent V1 at 50K cohort: +6% email creates/user, >99% significance).
- **Complication:** The overall FY26 stack is ~$32M short of $50M within a 12-month horizon. **R&A + Analytics AI cannot alone close $50M** — honest sizing puts Deepak's realistic share at **~$10-11M annualized (20-22%)**. The rest requires INFLUENCE partners (Personalization, SMS, Pricing) and ESCALATE asks (MM Account/Billing structural, Gainsight/CSM integration).
- **Question:** What should Deepak commission in R&A + AI Agent this quarter to drive the largest realistic share of the $50M, and what partner/SLT support is required to close the gap?
- **Answer:** **Lead with (1) scaling Analytics Agent V2 to the full paid base, (2) productizing Churn-Prediction insights inside Analytics Agent, and (3) shipping Annual Plans reporting in <4 weeks to unblock the Plans team's $1.3M-$3.9M FY27 bet. In parallel, escalate the MM Account/Billing structural ask and the Gainsight/CSM integration for churn prediction.**

---

## Deepak's share of $50M

| Tier | P50 | P90 | % of $50M |
|---|---|---|---|
| **OWN** (R&A + AI Agent) | **$10-11M** | $29M | 20-22% |
| **INFLUENCE** (Personalization, SMS, Pricing) | $9-10M | $18M | 18-20% |
| **ESCALATE** (MM structural, QBO bundle, Gainsight) | $4-5M | $20M | 9-10% |
| **TOTAL realistic (P50)** | **~$23-26M** | ~$67M | **~46-52%** |

Gap to $50M at P50: **~$24-27M** — requires either 18-24 month horizon OR aggressive new levers (consumption pricing, MM Premium tier, cross-Intuit bundling).

---

## Part 1 — Top 3 OWN-tier recommendations [Deepak commissions directly]

### #1 — Scale Analytics Agent V1 → V2 full paid base [OWN, Commit]

- **Mechanism:** V1 measured +6% email campaigns/user lift with >99% significance in a 50K cohort. Scaling to ~993K paid users with honest 75% lift attenuation = **~$4.0M P50 annualized**.
- **Business case:** P50 $4.0M / P90 $9.0M; probability 0.65; time to impact 9 months; score 3.5.
- **Pillars:** 5 High (Revenue, Strategy, Evidence, Execution, Compounding).
- **Capacity ask:** 1-2 HC AI Agent eng + inference-cost budget.
- **Partner dependencies:** SMS Growth (data pipe for V2 coverage), AI Science, DS.
- **Predicted metric movement (G14):** `email_creates/active-C1` +3-6% once V2 reaches ≥500K users; 180 days; `queries/31-email-creates.sql`.
- **Confidence:** High (one measured experiment).
- **What would change my mind:** V2 beta at 200K shows <1% lift (early saturation); Klaviyo Breeze ships parity before GA.
- **Pre-mortem:** Lift attenuation > expected; infra cost negative at scale; competitor response erases moat.
- **Next step:** Lock V2 ramp plan with Stephen Yu + Kuntal Naphade by **2026-05-12**.

### #2 — Productize Churn-Prediction insights in Analytics Agent [OWN, Commit]

- **Mechanism:** $76.5M annualized MRR-at-risk (active+passive). Surfacing propensity-model outputs in Agent (for C1s AND CSMs) enables onset-of-signal intervention. 15% recovery of actually-lost MRR = **~$5.5M P50 annualized**.
- **Business case:** P50 $5.5M / P90 $11M; probability 0.5; time to impact 6-9 months; score **4.4 (highest)**.
- **Pillars:** 3 High (Revenue, Strategy, Customer-problem) + 2 Medium.
- **Capacity ask:** 2-3 HC AI Agent eng + 1 DS allocation.
- **Partner dependencies:** DS (Ashish Prakash, Jeremy Diaz, Himanshu Dubey); ⚠️ **Gainsight/CSM integration is 2x multiplier — see ESCALATE #9**.
- **Predicted metric movement (G14):** Active churn MRR -5% to -10% within 12 months; `queries/22-active-churn-mrr.sql`.
- **Confidence:** Medium (cohort data strong; no concluded end-to-end experiment).
- **What would change my mind:** Propensity-model precision <60% in pilot (false-positive avalanche); Gainsight integration proves impossible.
- **Pre-mortem:** Precision problem; intervention fails; CSM pipe never lands.
- **Next step:** 2-week scoping sprint with Ashish Prakash to validate model precision on HVC cohort. Due **2026-05-19**.

### #3 — Annual Plans reporting & attribution accelerator [OWN, Commit]

- **Mechanism:** AP experiment live 2026-04-23 (predicted $1.3M-$3.9M FY27). R&A ships AP dashboard in <4 weeks → Plans team iterates 2x vs 1x in 12-week window → pulls 20-30% of FY27 impact into FY26.
- **Business case:** P50 $0.55M / P90 $1.0M; probability 0.75; time to impact 4-6 weeks; score 3.96. **Fastest-speed, lowest-capacity OWN bet.**
- **Pillars:** 2 High (Strategy, Time-to-impact) + 1 Strong evidence.
- **Capacity ask:** 1 R&A Eng + 1 data analyst; 2-week sprint.
- **Partner dependencies:** Plans PM (Jacquelyn Horgan), FinOps, DS (Ethan Ham).
- **Predicted metric movement (G14):** exp-to-readout time <14 days for AP experiment; 42 days; qualitative audit.
- **Confidence:** High (live experiment + straightforward build).
- **What would change my mind:** Plans PM doesn't share experiment spec in time; AP experiment fails to show signal.
- **Pre-mortem:** Wrong dashboard built; AP fails; build overruns.
- **Next step:** Request experiment-design doc from Jacquelyn Horgan by **2026-05-05**; target dashboard GA by **2026-05-19** (ahead of first read).

---

## Part 2 — Top 2 INFLUENCE-tier recommendations [Deepak co-sponsors with partner PMs]

### #6 — Personalization / CDP compound: next 2 primitives [INFLUENCE]

- **Partner PM:** Payton Camilli (Audience) + Frank Persico (Segmentation EM).
- **Expected contribution:** $4.9M × 0.65 = **$3.2M expected**.
- **R&A role:** Analytics Agent V2 consumes the new primitives → compounds with OWN #1.
- **Predicted metric:** `email_creates` +3% to +5%; 56 days.

### #7 — SMS credit-purchases decline diagnostic [INFLUENCE, POL/Probe]

- **Partner PM:** Connor Callahan (SMS Growth).
- **Mechanism:** `sms_credit_purchases` down 42.7% over 11 weeks. Defensive: protects $4.5M P50 SMS lever.
- **R&A role:** 3-day diagnostic dashboard.
- **Predicted metric:** >900/wk within 4 weeks OR flat-to-down; 28 days.

---

## Part 3 — ESCALATE tier (SLT decisions required)

### #8 — 🚨 Stand up MM Account/Billing structural workstream [ESCALATE]

- **Why escalate:** FY26 P1 for MM Subscription/Community with 0 structural launches in 9 months. Klaviyo + HubSpot have parity. Needs HC + capacity reallocation from SLT.
- **Expected:** $4.0M × 0.4 = $1.6M; long horizon 12-18 months.
- **R&A downstream:** unlocks Rec #8 (MM multi-entity reporting) in OWN tier.
- **Next step:** 2-week discovery (≤30 customer-conversations) BEFORE committing structural eng.

### #9 — 🚨 Gainsight / CSM integration for Churn-Prediction Agent [ESCALATE]

- **Why escalate:** Rec #2 has 2x leverage multiplier if Gainsight/CSM workflow integration lands. Currently coverage gap (Tier 1.2).
- **Expected value of integration landing:** moves Rec #2 from $5.5M to $11M P50; net uplift ~$5.5M.
- **Next step:** Deepak escalates to CS leadership; request joint scoping for H2 FY26.

---

## Prior-week prediction hit rate

**N/A — second run.** First-run predictions (2026-W17 rec-1, rec-2, rec-3 from v1) are still within their windows:
- rec-1 (email_creates +3-5%, 56d) — due 2026-06-23
- rec-2 (MM Premium bookings +20-35%, 365d) — due 2027-04-28
- rec-3 (SMS credit-purchases, 28d) — due 2026-05-26

Rolling 12-week hit rate: not yet established.

## New predictions written this run

**8 predictions** written to `predictions-ledger.jsonl` — 5 OWN, 2 INFLUENCE, 1 ESCALATE. See table in `07-recommendations.md`.

## Strategy-vs-Execution scorecard (unchanged this week)

| FY26 priority | Status | Evidence |
|---|---|---|
| P1 MM Account/Billing flex | **Stuck** (0 structural launches in 9 months) | Escalated in Rec #8 |
| P2 Channel Expansion (SMS, WhatsApp, social) | **Shipped+In-flight** | SMS 6 stacked wins; WhatsApp private beta |
| P3 Integrations & Data Enablement | **Shipped** (4 wins) | Joins Segment, x290, Sections, Meta CA |
| Ecomm P1 Personalization Depth | **Shipped** | Same 4 as P3; Shopify/BC/Woo parity gaps |
| Ecomm P2 Reporting & Attribution | **In-flight** | Analytics Agent V1; Rec #4 (OWN) addresses |
| Ecomm P3 Lead Ads | **Shipped (partial)** | Meta CA GA |
| Loyalty / UGC | **Stuck (correctly)** | FY27+ exploration |
| Advanced campaign management | **In-flight** | Frequency caps + multi-audience not visible |
| AI Agents / DFY | **Shipped (1 measured)** | Project Alfred V1; Rec #1 scales it |

## Open questions / escalations

- **🚨 Recommendation #8 escalation:** MM Account/Billing structural workstream needs HC/capacity decision.
- **🚨 Recommendation #9 escalation:** Gainsight/CSM integration for Rec #2 leverage multiplier.
- **Coverage gaps still hot:** Jira (Tier 1.1), Salesforce/Gainsight (1.2), Amplitude (1.3) — see `canon/coverage-gaps.md`.
- **Contradiction unresolved:** PDF `new_booking_timing` % vs BigQuery. Needs Finance reconciliation.

---

## Run metadata

- **Subagents invoked:** 12 (incl. new mc-ra-ai-opportunity-analyst)
- **Self-eval score (v2):** pending re-score with ownership-tier rubric
- **Predictions graded:** 0 (first-run predictions still within window)
- **New predictions written:** 8 (5 OWN, 2 INFLUENCE, 1 ESCALATE)
- **Contradictions logged:** 2 (carried from v1)
- **Escalation flags:** 2 (Rec #8, Rec #9)
