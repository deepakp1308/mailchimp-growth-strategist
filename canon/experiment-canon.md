# Canon — Experiment Registry

> **Status:** Canonical structure (rebuilt weekly by `mc-experiment-synthesizer` from `#mc-experimentation-xfn` + `#mailchimp-launched`).
> **Owner:** Phuong Trang (XFN driver) + experiment owners
> **Last updated:** 2026-04-28

This file holds the canonical experiment registry. The agent appends new experiments to `knowledge/slack/` daily and synthesizes here weekly.

---

## Schema

| Field | Type | Description |
|---|---|---|
| `xid` | string | e.g. `x290`, `x287`, `xTBD` |
| `title` | string | short experiment title |
| `area` | string | Audience / Email / SMS / CJB / Automations / Growth / Identity / OBX / etc. |
| `owner` | string | DRI from Slack |
| `eng_lead` | string | engineering lead |
| `ds_lead` | string | data science lead |
| `hypothesis` | string | what we expected to see |
| `primary_metric` | string | metric being moved |
| `baseline` | float | pre-experiment baseline |
| `target_lift` | float | target % lift |
| `actual_lift` | float? | observed % lift (null until concluded) |
| `secondary_metrics` | string[] | other tracked metrics |
| `guardrails` | string[] | guardrail metrics |
| `start_date` | date | |
| `end_date` | date? | |
| `decision` | enum | `running` / `concluded-shipped` / `concluded-killed` / `concluded-iterated` / `inconclusive` |
| `classification` | enum | `clear-win` / `clear-loss` / `neutral` / `inconclusive` |
| `dollar_impact_fy26` | float? | $ impact in current fiscal year |
| `dollar_impact_fy27` | float? | annualized $ impact |
| `fy26_priority_match` | string[] | which FY26 priorities this addresses (from `fy26-strategy.md`) |
| `icp_match` | string[] | which ICPs benefit |
| `slack_anchor_ts` | string | TS of original Slack post (`#mailchimp-launched` or `#mc-experimentation-xfn`) |
| `edd_link` | string | link to EDD doc |
| `dashboard_link` | string | results dashboard |

---

## Seed experiments (from this thread's data — populated 2026-04-28)

> The agent will rebuild this list weekly. This is the initial seed.

### Concluded — clear wins

| xid | Title | Area | Owner | Lift | $ Impact | FY26 priority match |
|---|---|---|---|---|---|---|
| x290 | Inline Contact Search in Audience | Audience | Payton Camilli | +2.91% campaign creation rate (7d post-search) | not yet annualized | Personalization / Integrations |
| x287 | Recommend SMS to C1s with C2 Phone Numbers | Audience+SMS | Connor Callahan | +37.9% SMS purchase rate (vs control) | $230K FY26 / $1.2M FY27, +2,000 net new SMS bookings | SMS Expansion / Channels |
| Sections Manager | Nuni Sections Manager | Email | Ose Amiegheme | clear win on C1 send rate, +845 weekly C1 senders | $20K FY26 in-year / $145K annualized | Email Modernization |
| Joins Segment Trigger | Automation Flows new trigger | Automations | Elizabeth Bertasi | shipped 2026-04-28; pre-experiment hypothesis based on 2023 HVC churn report (~10% automations-related churned users, ~20% churned revenue) | TBD | Personalization / Automations |
| OTP Code at Activation | Email OTP at account activation | Identity | Margarita Caraballo | +3.74% activation rate, -33% session friction | TBD (revenue impact still being measured) | DFY Onboarding / Activation |

### Running (live as of 2026-04-28)

| xid | Title | Area | Owner | Started | Target | FY26 priority match |
|---|---|---|---|---|---|---|
| (TBD) | Annual Plans Self-Serve | PLC + Dotcom | Jacquelyn Horgan | 2026-04-23 | AP take rate >10%, +2.5% prospect-to-booking, +3pts 90d retention | Pricing/Packaging |
| WhatsApp Private Beta | WhatsApp launch | Messaging | Devin Mercier | 2026-03-11 | activation rates, campaign perf vs SMS, credit purchase | MM Channels |
| x202 | Email Image Normalization | Email | Devin Mercier | concluded readout 2026-10-14 | results readout — re-classify | Email Modernization |
| x471 | Done-For-You-GTKM-Profile (shadow) | OBX | Joshua Fischer + Jeevisha Anandani | (planning) | onboarding completion | DFY Agentic AI |
| x472 | Focused & Payoff-Based Checklist | OBX | Joshua Fischer + Shakib Ahmed | (planning) | onboarding completion + payoff | DFY Agentic AI |
| x488 | Showing DA and Search Side-by-Side | Support | Sonia Singhal + Dev Parikh | (planning) | support efficiency | DFY Agentic AI |

### Cumulative SMS Growth Impact (per Connor Callahan, 2026-03-20)

- 6 winning experiments stacked
- 9,300+ bookings expected in FY26
- +45 bps to SMS penetration
- $1.08M FY26 / $3.96M FY27

---

## Pattern detection (initial)

Areas with consistent winners:

- **Personalization layer** (CDP + segmentation + behavioral triggers) — x290, x287, Joins Segment, Sections Manager
- **SMS expansion** — 6 cumulative winners
- **Email modernization** — Sections Manager, Image Normalization
- **Activation onboarding** — OTP, DFY-GTKM, Focused Checklist (early signs)

Areas where results are mixed/pending:

- **Annual Plans / pricing experiments** — first-ever rate-card test, results due ~2026-05-21
- **WhatsApp** — private beta only, public beta target July 2026; revenue signal premature

Areas underrepresented in active experimentation:

- **MM Account Structure & Billing flexibility** (Priority 1 in FY26 narrative for MM Subscription/Community) — no x-id experiments visible in window
- **Lead Ads (Meta + Google)** — narrative-level only; no live experiment seen
- **Loyalty / Reviews / UGC** (Ecomm exploration priority) — no live experiment seen

This gap signals strategy-execution misalignment that the Strategy Reconciler should flag.
