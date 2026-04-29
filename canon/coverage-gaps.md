# Canon — Coverage Gaps & MCP Integration Roadmap

> **Status:** Canonical. Agent reads, never invents.
> **Last updated:** 2026-04-28 (Phase 6 — first benchmark run)

This file tracks **data sources NOT YET piped into the agent**. The orchestrator should surface these gaps proactively in every quarterly review, and the agent should explicitly tag findings as Low-Confidence when they depend on a missing source.

Gaps are ranked by **(impact_on_recommendation_quality × ease_of_integration)** so that the highest-leverage closures come first.

---

## Tier 1 — High impact, moderate effort

### 1.1 Jira / Productboard — Roadmap source-of-truth
- **Why critical:** Without Jira, the **Strategy ↔ Execution Reconciler** depends entirely on Slack signal to identify "in-flight" work. We undercount active investments and overcount "stuck" priorities. Specifically: the FY26 P1 MM Account/Billing-flex stuck-claim cannot be validated without Jira.
- **Integration path:** Cursor MCP for Jira (look for `jira-mcp` / Atlassian-published MCP) OR scrape via Jira REST API with a personal access token.
- **What to query:** Open epics tagged with FY26 priority labels; project boards for Plans/PLC, Identity, Audience/CDP, Email, SMS Growth, Onboarding, Analytics Agent.
- **Estimated agent uplift:** Strategy Reconciler confidence Medium → High. Could reveal 1-3 hidden in-flight workstreams per quarterly review.
- **Gap signaling in current run:** 01-strategy-reconciliation.md, "Open questions / data gaps" section. Recommendation #2 (MM structural) accuracy gated on this.
- **Effort estimate:** 2-3 days (auth setup + Jira project mapping + 5-10 canonical JQL queries in `queries/` directory).

### 1.2 Salesforce / Gainsight — Sales pipeline + CSM ledger
- **Why critical:** MM acquisition lever (FY26 GTM #2) cannot be quantified without sales pipeline view. CSM-managed customer health (per WhatsApp Private Beta context: "20 CSM-managed customers") is invisible. Win/loss reasons not piped.
- **Integration path:** Salesforce REST API (likely a `salesforce-mcp` available; or build via SOQL client). Gainsight has REST API + Cursor IDE Browser fallback.
- **What to query:** MM ($299+ MRR) account list with stage, predicted ARR, churn-risk score; SDR/AE outbound metrics; agency partner attribution; CSM notes for HVC accounts.
- **Estimated agent uplift:** GTM Lever Analyst MM-acquisition confidence Low → Medium-High. Adds ~$5M-$15M of MM-specific dollar visibility.
- **Gap signaling in current run:** 04-gtm-levers.md Lever 2 marked "Target unknown."
- **Effort estimate:** 4-5 days (auth + SOQL queries + entitlement scoping).

### 1.3 Amplitude / Pendo — Product analytics with cohort granularity
- **Why critical:** `bi_aggregate.*` is great for week-grain rollups, but lacks session-level granularity for funnel and feature-adoption deep-dives. Specifically: the Personalization/CDP compound's "saturation" risk (per Adversarial Review headline finding) needs per-feature-primitive adoption curves we can only get from Amplitude.
- **Integration path:** Amplitude REST API (`amplitude-mcp` may exist) OR Pendo API. Cursor IDE Browser as fallback for Tableau-published Pendo dashboards.
- **What to query:** Funnel for each personalization primitive (Joins Segment, Inline Search, Sections Manager, Meta CA); cohort retention by feature-adopter; rage-click telemetry per surface.
- **Estimated agent uplift:** Recommendation Ranker Pillar P4 (Evidence quality) confidence increase. Specifically helps detect saturation BEFORE it shows up in `email_creates` aggregate.
- **Gap signaling in current run:** 06-growth-tree.md Lever #1 saturation risk; 08-qc-report.md adversarial finding.
- **Effort estimate:** 3-4 days.

---

## Tier 2 — High impact, higher effort

### 2.1 QBO data — Cross-Intuit referral/bundle opportunity
- **Why critical:** FY26 narrative explicitly cites QBO+MC as FY27+ exploration. Without QBO data, cannot quantify the cross-pollination revenue opportunity (Growth Tree's #5 candidate-new lever, est $5M-$15M).
- **Integration path:** Internal Intuit data lake. Likely needs `qbo` and/or `qbo_datastorage` BigQuery dataset access (already in dataset list). Coordinate with Finance/FDTG.
- **What to query:** Overlap of QBO + MC customers; QBO customer industry mix; conversion rate on cross-product referrals.
- **Estimated agent uplift:** Adds defensible-moat candidate-new lever to the Growth Tree.
- **Gap signaling in current run:** 06-growth-tree.md "Candidate NEW levers" #4.
- **Effort estimate:** 1-2 weeks (cross-team data access agreements).

### 2.2 Gong / Heymarvin / Chorus — Customer interview corpus
- **Why critical:** Recommendation #2 (MM Account/Billing structural) hypothesizes that MM customers churn over billing infrastructure. Without win/loss interview transcripts, this is narrative, not validated need. Per Bethany McDaniel's Sections Manager thread (2026-03-31), Heymarvin is already used for UXR — should pipe.
- **Integration path:** Gong REST API; Heymarvin has API; Chorus has API. May need DPO sign-off for transcript ingestion.
- **What to query:** Top 50 most-recent MM-customer churn-call transcripts; top 20 Premium-tier recent win-call transcripts; thematic tagging (billing, feature, pricing, support).
- **Estimated agent uplift:** Recommendation Ranker Pillar P3 (Customer-problem severity) confidence Low → High for MM-acquisition recommendations.
- **Gap signaling in current run:** 07-recommendations.md Recommendation #2 "What would change my mind" section.
- **Effort estimate:** 1-2 weeks (DPO + auth + entitlement).

### 2.3 Tableau / Looker — pre-curated Finance/Marketing dashboards
- **Why critical:** Finance-blessed numbers (e.g., FY26 target curves) are typically published as Tableau dashboards. Cross-checking BigQuery against Tableau is the proven contradiction-catching pattern.
- **Integration path:** Tableau REST API (well-documented) OR Cursor IDE Browser screenshot capture. Looker has REST API too.
- **What to query:** Specific dashboards: Mailchimp Product Health (already PDF-parsed), `% Churn Overview`, ICP-Cohort lifecycle dashboards, Finance MBR dashboard.
- **Estimated agent uplift:** Numeric Round-Tripper (mc-numeric-round-tripper) gets a 3rd-source cross-check. Catches more drifts.
- **Gap signaling in current run:** contradictions.md (PDF dashboard `new_booking_timing` % vs BigQuery dispute).
- **Effort estimate:** 3-5 days.

---

## Tier 3 — Lower impact, lower effort (quick wins)

### 3.1 `% Churn Overview.xlsx` xlsx parsing
- **Why critical:** Finance-curated artifact already on disk. Just needs `openpyxl` install + a one-time parse. Already referenced in `mc-doc-parser` SKILL.
- **Integration path:** `pip install --user openpyxl` (one-time). Then `mc-doc-parser` runs it every cycle.
- **Estimated agent uplift:** Cohort Churn Diagnostician gets 3rd-source cross-check.
- **Effort estimate:** 30 minutes.

### 3.2 `bi_finance.new_bookings_targets` / `paid_users_targets` queries
- **Why critical:** FY26 target curves are needed to compute "% to target" precisely. Currently using narrative-quoted targets (e.g., "$3.1M FY26 scaled acquisition") rather than live target tables.
- **Integration path:** Add 2 SQL templates to `queries/` (`70-target-bookings.sql`, `71-target-paid-users.sql`).
- **Estimated agent uplift:** Strategy Reconciler "% to target" precision; GTM Lever Analyst pacing visibility.
- **Effort estimate:** 1-2 hours.

### 3.3 SMS daily-rollup table (`bi_aggregate.sms_*`?)
- **Why critical:** SMS credit purchases declining trend (Recommendation #3) needs per-cohort breakdown to root-cause. Daily rollup likely exists in `bi_reporting.sms_daily_rollup` (verified in dataset list).
- **Integration path:** Add SQL template for cohort-by-tenure × SMS purchase pattern.
- **Estimated agent uplift:** Recommendation #3 prediction-grading sharper.
- **Effort estimate:** 1 hour.

### 3.4 `#mc-competitive-intelligence` Slack channel
- **Why critical:** Currently in coverage-gap. `mc-external-researcher` would benefit from internal channel signal.
- **Integration path:** Add channel ID to `mc-slack-harvester` channel registry.
- **Estimated agent uplift:** Competitive Intel Analyst confidence Low → Medium.
- **Effort estimate:** 5 minutes.

### 3.5 Connor Callahan's "Watchtower" output
- **Why critical:** Already publishes SMS regulation alerts to GitHub Pages + a Slack channel. Pipe its output into `knowledge/external/regulation/` rather than re-scraping.
- **Integration path:** Add Watchtower's GitHub Pages URL to `mc-external-researcher` source list.
- **Estimated agent uplift:** Eliminates duplicate work; concentrates regulatory signal.
- **Effort estimate:** 30 minutes.

---

## How the agent should reference this file

In every recommendation that depends on a missing source, the agent should:

1. State the dependency explicitly in "What would change my mind" or in `08-qc-report.md`.
2. Tag confidence accordingly (e.g., "Low — depends on win/loss data not yet piped, see canon/coverage-gaps.md §2.2").
3. In quarterly reviews, surface a **Coverage-Gap Closure Backlog** section in the executive brief, ranked by impact-on-recommendation-quality.

## How Deepak should use this file

Treat it as a **work-prioritization input**: pick 1-2 gaps to close per quarter based on which recommendations are currently most-bottlenecked.

For Q3 FY26 (most likely next 13 weeks), the highest-leverage closures are:
- **Tier 3.1** (xlsx parse) — 30 min, immediate cross-check value
- **Tier 3.2** (target queries) — 1-2 hr, sharpens every weekly run
- **Tier 1.1** (Jira) — 2-3 days, unlocks Strategy Reconciler confidence
- **Tier 2.2** (Gong/Heymarvin) — validates Recommendation #2 in time for capacity decision

If forced to pick ONE: **Jira integration (Tier 1.1)**. It immediately validates 9 months of "in-flight" claims and either confirms or refutes the "MM Account/Billing stuck" finding that's driving Recommendation #2.
