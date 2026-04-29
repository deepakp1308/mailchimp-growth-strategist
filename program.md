# Program — Current Research Agenda

> **This is the single human-edited control surface for the Mailchimp Growth Strategist agent.**
> The orchestrator reads this file FIRST on every run. It frames the entire iteration loop.
> Borrowed from `karpathy/autoresearch`'s `program.md` pattern.

**Owner:** Deepak Prabhakaran (PM, Reporting & Analytics + AI Agent)
**Last updated:** 2026-04-28
**Status:** Active

---

## 1. Headline Question

**How does Mailchimp add $50M incremental revenue on top of current FY26 trajectory, within the next 12-18 months?**

Sub-questions to keep front and center:

- Where in the **Growth Tree** (Paid Users × ARPU × (1 - Churn) × (1 + Expansion)) is the largest realistic delta?
- Which **FY26 priorities are actually moving** the metrics they were supposed to move?
- Which **launched features/experiments** are paying off vs. underperforming?
- Where are we **shipping things not in the plan** (and why)?
- Which **cohorts/segments** are most underserved relative to FY26 targets?

---

## 2. Active Hypotheses Being Tested

| # | Hypothesis | Where to look | Confidence prior |
|---|---|---|---|
| H1 | Annual Plans (live experiment as of 2026-04-23) is the single largest near-term lever — could deliver $1.3M-$3.9M FY27 incremental on its own | `bi_finance.daily_bookings`, `#mailchimp-launched` Apr 23 thread, AP take rate dashboard | Medium-High |
| H2 | Active churn reduction has higher leverage than activation rate increase, given current base rates (CP active churn rate ~0.95% weekly vs. ~52% Paid WAU rate) | `bi_aggregate.churn_daily`, `% Churn Overview.xlsx` | Medium |
| H3 | SMS expansion is the single largest expansion-revenue driver — 6 winning experiments stacked = $1.08M FY26 / $3.96M FY27 | `bi_aggregate.product_health_weekly` (sms_*), `#mailchimp-launched` SMS posts | High |
| H4 | MM acquisition is structurally underweighted — FY26 narrative says it's a priority but launches and experiments skew SMB | `#mailchimp-launched` segmentation, `bi_finance.daily_bookings` `tier_size` field | Medium |
| H5 | WhatsApp will not move the needle in FY26 (still in private beta as of 2026-03-20, public beta target July 2026) | `#mailchimp-launched` Mar 20, beta cohort metrics | High |
| H6 | The personalization play (CDP + Pixel + Inline Search + Joins Segment) is the strongest *capability* compound — winners cluster here | `#mc-experimentation-xfn` portfolio, experiment IDs x290, x287, Joins Segment | Medium-High |
| H7 | "Done-for-you" agentic AI (Analytics Agent v1, Acquisition Agent in development) has not yet shown measurable revenue impact — claims of 6% lift in email creates need to be re-validated at scale | Project Alfred 2026-03-13 thread, `bi_aggregate.product_health_weekly` (email_creates) | Low (claims-pending-verification) |

The agent should **continuously re-evaluate** these and propose new hypotheses.

---

## 3. Hand-Edited Guardrails

The agent **must** respect these on every run:

1. **Decisions about Reporting & Analytics surface or AI Agent surface require Deepak's explicit approval** — agent recommends, never commits.
2. **Recommendations that displace Analytics Agent GA, touch QBO/Omni scope, or imply HC change** must be flagged with the Escalation triggers from `ra-dependency-evaluator`.
3. **Customer names from Slack stay in `knowledge/`** — never in published briefs or dashboards.
4. **No vibes-based recommendations** — every rec needs ≥1 Pillar at High with a named mechanism.
5. **No silent revisions** — if this week contradicts last week, log it in `contradictions.md` with explicit resolution.
6. **No new analytical agendas** — if you discover something interesting outside this `program.md`, add it to "candidate hypotheses" below, do not pursue it without my edit.

---

## 4. Things the Agent Should NOT Assume

- ❌ Do not assume current Mailchimp pricing tiers without checking `bi_finance.payg_historical_rate_card` and the latest plan-selector flow.
- ❌ Do not assume `bi_aggregate.product_health_weekly.email_creates` includes SMS or CJB creates — it doesn't (those are separate columns).
- ❌ Do not assume "active churn" and "passive churn" use the same denominator — they don't (cross-check `metrics-canon.md`).
- ❌ Do not assume Tableau dashboard numbers === BigQuery actuals — there's known lag/transformation drift; surface conflicts in `contradictions.md`.
- ❌ Do not assume FY26 narrative numbers (e.g. "+$3.1M scaled acquisition target") are tracking — verify against `bi_finance.new_bookings_targets`.
- ❌ Do not assume team owners — only use names from `canon/org-glossary.md`.
- ❌ Do not assume the Annual Plans experiment (live 2026-04-23) has results yet — it's a 4-week test; first reads available ~2026-05-21.

---

## 5. Candidate Hypotheses (for human review — do not pursue without explicit edit)

> Agent: when you discover something worth investigating, add it here as a comment. Do NOT pursue it as if it's an active hypothesis until I move it to §2.

*(empty — agent will append candidates here over time)*

---

## 6. Run Configuration

- **Weekly cadence**: Monday 7am PT
- **Active Slack channels**: `#mailchimp-launched` (C03TLJNADSP), `#mc-experimentation-xfn` (C095TT75VTQ), `#mc-hvc-escalations` (C095FJ3SQF4), `#mc-reporting-analytics-feedback` (C06SW7512P2)
- **Active BigQuery datasets**: `bi_aggregate.*`, `bi_finance.*`, `bi_product.*`
- **Active doc sources**: `FY26 Strategic Narrative_Mailchimp_vFINAL.pdf`, `Executive Overview (All Users).pdf`, `% Churn Overview.xlsx`
- **Output channels**: Slack DM to W8FL6URHQ + GH Pages dashboard + repo `analyses/YYYY-WW/`
- **Token budget per run**: ~500K (orchestrator + ~10 subagents @ ~50K each)
- **Self-eval gate**: ≥20/25 to publish (hard floor)
- **Prediction-grading**: required before generating new predictions (G15)
test-tier1-human-only
