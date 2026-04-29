# Strategy ↔ Execution Reconciliation — 2026-W17

**Run timestamp:** 2026-04-28 (PDT)
**Window:** Aug 1, 2025 → Apr 28, 2026 (full FY26 to date — 9 months)
**Source data:** `knowledge/slack/_seed_transcript.md` (264 top-level launch posts), `canon/fy26-strategy.md`

## Summary

| Status | Count | % of 9 priorities |
|---|---|---|
| Planned-and-Shipped (P&S) | 4 | 44% |
| Planned-and-In-Flight (P&IF) | 3 | 33% |
| Planned-but-Stuck (PBS) | 2 | 22% |
| Shipped-but-not-Planned (S¬P) | ~7 distinct themes | (separate count) |

**Headline finding:** **MM Account/Billing flexibility (FY26 P1 for MM Subscription/Community)** is the single most under-shipped priority — only one experiment (Annual Plans) addresses it, and that's a pricing experiment, not the structural billing infrastructure (multi-entity, ACH/wire, parent-child) the narrative calls for.

---

## By Priority

### MM Subscription + Community

#### Priority 1 — MM Account Structure & Billing Flexibility — **PBS**
- **Evidence found**:
  - Annual Plans Self-Serve Experiment (live 2026-04-23, Slack TS 1776958294, owner Jacquelyn Horgan) — **partial fit** (pricing/billing-term, not infrastructure)
  - Place of Supply-Based Taxation (2026-04-22, Slack TS 1776862994, owner Jacquelyn Horgan) — billing infrastructure; compliance-driven, not MM-flex-driven
- **Gaps**: NO launches/experiments visible for: multi-entity, parent-child accounts, SSO login, automated multi-entity/multi-location billing, wire/ACH transfers, contracts and contract price lock, role-based permissions
- **Confidence**: **Medium** (we may be missing in-flight Jira items not announced in Slack)
- **Risk callout**: This is FY26 P1 for MM Subscription + Community ICPs. With Klaviyo and HubSpot offering full multi-entity + role-based + SSO at the MM tier, parity gap is widening every week.

#### Priority 2 — Channel Expansion — **P&S + P&IF**
- **Evidence found**:
  - WhatsApp Private Beta launched 2026-03-11 (Slack TS 1774026751, owner Devin Mercier) — Private beta (~20 customers), Public beta target July 2026
  - SMS Growth: 6 stacked winning experiments cumulatively driving $1.08M FY26 / $3.96M FY27, +45 bps SMS penetration (per Connor Callahan 2026-03-20, Slack TS 1774008120)
  - SMS x287: Recommend SMS to C1s with C2 Phone Numbers (concluded clear-win 2026-03-20: $230K FY26, $1.2M FY27)
- **Gaps**:
  - Social posts (LinkedIn, TikTok, IG retargeting) — no launches found
  - SMS standalone offering (without email) — referenced in FY26 narrative as a P2, no evidence yet
- **Confidence**: **High** for SMS stack; **Medium** for WhatsApp (private beta only)

#### Priority 3 — Integrations & Data Enablement — **P&S**
- **Evidence found**:
  - Joins Segment Trigger in Automation Flows (2026-04-28, Slack TS 1777383920, owner Elizabeth Bertasi) — directly enables CDP/Segmentation activation
  - x290 Inline Contact Search in Audience (clear-win 2026-04-27 ramped 100%, Slack TS 1776205376, +2.91% campaign creation rate, owner Payton Camilli)
  - Meta Custom Audience Integration GA (2026-04-21, Slack TS 1776776408, owner Srilekha Chandrashekar) — direct sync between MC segments and Meta retargeting
- **Gaps**:
  - Behavior/identity tracking pixel: referenced but no public launch yet
  - GA / FullContacts / Gmail sync: no launches found
  - API / developer portal modernization: no launches found
- **Confidence**: **High** for what's shipped; **Medium** on what's on the way

---

### Small/LMM Ecomm

#### Priority 1 — Personalization Depth via Integrations — **P&S**
- **Evidence found**:
  - Meta Custom Audience Integration GA (2026-04-21) — strong personalization play
  - Joins Segment Trigger (2026-04-28) — enables behavioral re-engagement at automation level
  - Nuni Sections Manager (2026-03-31, Ose Amiegheme, Slack TS 1774972805) — content reusability driving +845 weekly C1 senders, $20K FY26 / $145K annualized
  - Email OTP at activation (2026-04-27 readout, Margarita Caraballo, +3.74% activation rate)
- **Gaps**:
  - BigCommerce / WooCommerce parity with Shopify: not visible
  - Promo codes (static + dynamic): not visible
- **Confidence**: **Medium-High**

#### Priority 2 — Marketing ROI through Reporting & Attribution — **P&IF (mostly)**
- **Evidence found**:
  - Analytics Agent V1 (Project Alfred) test update (2026-03-13, Stephen Yu) — +6% email campaigns/user, 3000+ insights generated, $1,300 MRR HVC custom request solved instantly
  - Conversion Insights dashboard work (referenced in `#mc-experimentation-xfn` 2025-10-21)
  - New attribution defaults experiment (referenced 2025-08-19, Nicole Jayne)
- **Gaps**:
  - GMV / Ecomm-specific revenue attribution: no clear launch
  - Predictive churn/upsell analytics: surfaced via Analytics Agent but not dedicated experiment
- **Confidence**: **Medium**
- **Note**: Analytics Agent V1 is YOUR (Deepak's) primary surface — see escalation rules.

#### Priority 3 — Lead Ads — **P&S (partial)**
- **Evidence found**:
  - Meta Custom Audience Integration GA (2026-04-21) — supports lead ads use case
  - Builtwith intent integration experiment (2025-08-05 readout, Andrew Spitz, Slack TS 1754412964)
- **Gaps**:
  - Google Lead Ads: not visible
  - LinkedIn / Pinterest / Snap / TikTok / Reddit lead ads: not visible (FY27+ per narrative — OK)
- **Confidence**: **Medium**

#### Exploration — Retention & Loyalty — **PBS**
- **Evidence found**: NONE
- **Gaps**: Loyalty/rewards, referrals, product reviews/UGC, AI unified inbox — all FY27+ exploration per narrative; OK to be PBS for FY26
- **Confidence**: High (correctly deprioritized)

---

### Segment-agnostic Agentic AI / DFY

#### Priority 1 — Advanced Campaign Management — **P&IF**
- **Evidence found**:
  - Joins Segment trigger (2026-04-28) — enables dynamic content via segment-driven automation
  - Nuni Sections Manager (2026-03-31) — content blocks, foundation for "reuse blocks across campaigns"
- **Gaps**:
  - Frequency caps for email/SMS: not visible
  - Multi-audience send: not visible
  - Dynamic content for email components: foundation laid by Sections Manager but not the full feature
- **Confidence**: **Medium**

#### Priority 2 — AI Agents — **P&S + P&IF**
- **Evidence found**:
  - Analytics Agent V1 (Project Alfred) test live with 50K cohort (2026-03-13)
  - DFY-GTKM-Profile experiment (Joshua Fischer + Jeevisha Anandani, planned 2026-04-21)
  - Focused & Payoff-Based Checklist experiment (x472, Joshua Fischer + Shakib Ahmed, planned 2026-04-21)
  - Showing DA and Search Side-by-Side (x488, Sonia Singhal + Dev Parikh, planned 2026-04-21)
  - Acquisition Agent (referenced in WhatsApp launch context 2026-03-20)
- **Gaps**: Full-stack DFY use-cases (channel-optimized templates with predictive personalization, automated campaign generation, lead scoring with intent-based automations) — early-stage only
- **Confidence**: **Medium**; agentic momentum is real but most is still pre-revenue

---

## Shipped-but-not-Planned (S¬P)

| Launch | Date | Owner | Why not in FY26 narrative? |
|---|---|---|---|
| Place of Supply tax compliance | 2026-04-22 | Jacquelyn Horgan | Compliance/risk, not in growth narrative — necessary table stakes |
| GSSO Escape Hatch | 2025-08-01 | Chima Okechukwu | Customer-pain hot fix (existing customers stuck), not strategic |
| The Watchtower (SMS regulation monitor) | 2026-04-20 | Connor Callahan | Internal AI tooling — pattern transferable but not in FY26 |
| Email OTP at Activation | 2026-04-27 | Margarita Caraballo | Activation lift; aligns with DFY onboarding spirit but not explicit in plan |
| Inline Contact Search in Audience (x290) | 2026-04-14 | Payton Camilli | Data activation; aligns with P3 Integrations but emerged from team's own backlog |
| IPS (Intuit Persistence Services) launches | 2026-04-23 | Crystal Ju (Intuit-platform) | Cross-Intuit infra, not MC narrative |
| Multiple Identity Team improvements | various | Margarita Caraballo team | Foundational — not strategic-narrative line items |

---

## Notable patterns

1. **The "Personalization compound"**: 4 of the highest-leverage shipped wins (Joins Segment, Sections Manager, Inline Search, Meta Custom Audience) all live at the **CDP + Segmentation + Behavioral-trigger** layer. This is the strongest *cluster of evidence* in the entire portfolio. **Implication**: this is a real defensible capability stack worth doubling down on.

2. **The "MM gap"**: For an ICP that's HIGH value (per FY26) and where competitors (Klaviyo, HubSpot) have deep parity in MM-specific features (multi-entity, SSO, contracts), Mailchimp shipped **0 MM-specific account/billing infrastructure** in 9 months. The Annual Plans experiment is welcome but is a pricing+billing-term move, not the deeper structural work.

3. **The "agentic gap"**: Only Analytics Agent V1 has measured production impact (+6% email creates among 50K cohort). Acquisition Agent and DFY onboarding agents are still pre-revenue. The FY26 narrative implies more aggressive deployment.

4. **The "Free → Paid puzzle"**: From `bi_aggregate.bookings_weekly` (week 4/19): `free to paid` = 2,268 users (43% of bookings) vs. `immediate to paid` = 2,627 users (50%). The PDF dashboard claims "FT rolloff share = 9.39% CP" which uses a different definition. **Action item:** reconcile PDF dashboard `new_booking_timing` definition vs. BigQuery — likely log a contradiction.

---

## Open questions / data gaps

- **No Jira MCP**: cannot validate "in-flight" status reliably; depending on Slack signal alone undercounts active work.
- **No Productboard / roadmap source-of-truth**: same gap.
- **MM customer list size cuts**: the `bi_aggregate.bookings_weekly` `package` and `is_high_value` fields don't give us a clean MM proxy without an industry-vertical join.
- **FY26 P1 (MM Account/Billing) status**: cannot tell if it's "in-flight but-quiet" vs. "actually stuck."

---

## Findings ledger row written

```json
{"ts":"2026-04-28T21:00:00Z","source":"mc-strategy-execution-reconciler","claim":"FY26 priorities: P&S=4, P&IF=3, PBS=2; biggest gap: MM Account/Billing flex (P1 with zero structural launches in 9 months); strongest cluster: Personalization+Integrations (4 stacked wins)","confidence":"medium","citations":["analyses/2026-W17/01-strategy-reconciliation.md","canon/fy26-strategy.md","knowledge/slack/_seed_transcript.md"]}
```
