# Canon — R&A + Analytics AI Agent Product Surface

> **Status:** Canonical. Agent reads, never invents.
> **Owner:** Deepak Prabhakaran (PM, Reporting & Analytics + AI Agent)
> **Last updated:** 2026-04-29

This is **Deepak's primary ownership domain.** Recommendations that operate in this surface are **first-priority** for every weekly run (per `program.md §1`).

The Growth Strategist's `mc-recommendation-ranker` tiers recs as:

| Tier | Definition | Who commissions |
|---|---|---|
| **OWN** | R&A + AI Agent surface (scoped below). Deepak can directly commission. | Deepak + direct reports |
| **INFLUENCE** | Adjacent surface (Audience/CDP, SMS, Email, Plans, OBX) where R&A is a consumer OR provides the reporting layer. Deepak influences via PM partnership. | Partner PM + Deepak co-sponsors |
| **ESCALATE** | Out-of-scope: Plans/PLC structural, QBO/Omni, HC changes, AI archetype pivots. Needs SLT decision. | SLT / Deepak surfaces |

---

## Surface area definition (OWN tier)

### 1. Reporting product (the "R" in R&A)

Core reporting experiences the C1 sees inside Mailchimp:

- **Summary dashboards** — per-campaign, per-journey summary pages (`/summary/*`)
- **Recipient Activity** — `/opened/*`, `/click/*`, individual-level engagement
- **Click Performance** — click maps, link performance
- **Email Analytics** — overall account-level email KPIs
- **Custom Reports** — exportable/scheduled reports
- **Marketing Dashboard** — cross-product KPI rollup
- **SMS Reporting** — SMS-specific dashboards (dedicated R&A work after SMS-Growth ships the data)
- **CJB Reporting** — journey-level reporting
- **Export/Download workflows** — CSV, XLSX, PDF outputs

### 2. Attribution & Measurement

- **Revenue attribution** (ecomm + non-ecomm)
- **Cross-channel attribution** (email + SMS + WhatsApp + social)
- **Touchpoint sequencing**
- **A/B test + multivariate readouts**
- **Ecomm-specific metrics**: GMV, order count, ROI per campaign, per-subscriber value
- **Conversion goal attribution** (subscription-renewal, donation, purchase, etc.)

### 3. Analytics Agent (the "AI Agent" in R&A + AI Agent)

Deepak's other primary surface — codename **Project Alfred** internally.

- **Current V1** (live to 50K cohort per Stephen Yu readout 2026-03-13):
  - +6% email campaigns sent per user (2.69 → 2.86, >99% prob to beat control)
  - +0.7% % of users sending 1+ email campaigns (70.1% → 70.6%)
  - 85% engagement when users viewed Analytics Agent
  - 3,000+ insights generated to date
  - Custom HVC analytics request solved instantly vs. weeks
- **V2 (beta) scope** (per V1 readout):
  - Expanded data coverage (SMS, Ecomm funnel)
  - Enhanced data understanding layer (improved eval + accuracy)
  - Improved user context (C1 profile info)
  - Enhanced UX: streaming, conversation history, data visualizations
- **Future V3+ candidates**:
  - Churn-prediction insights surfaced in the Agent
  - Upsell/expansion opportunity insights
  - Predictive A/B test recommendations
  - "Why am I losing customers" DFY diagnostic agent
  - Vertical-specialized insights (Civic, Ecomm, SaaS)

### 4. Data foundations (where R&A intersects with data infrastructure)

- **`bi_aggregate.*` and `bi_product.*` BigQuery datasets** — R&A is the biggest consumer
- **CDP / Unified C2 Profile outputs** — R&A surfaces these
- **Event pipeline to reporting stores** — R&A is downstream consumer
- **Churn, MRR, tenure metrics** — R&A is the surfacer (dashboards + Analytics Agent)

---

## INFLUENCE tier (R&A is consumer / provides reporting layer)

| Partner surface | Partner PM | R&A role |
|---|---|---|
| **Audience / CDP** | Payton Camilli | R&A consumes CDP data for reporting + Analytics Agent; co-design CDP insights |
| **Segmentation** | Frank Persico (EM) | R&A consumes segmentation for audience-cohort reports |
| **Email (Nuni editor)** | Devin Mercier / Joshua Fischer | R&A provides Email Analytics reporting |
| **SMS Growth** | Connor Callahan | R&A provides SMS Reporting (post-SMS-Growth data pipe) |
| **Automations / CJB** | Elizabeth Bertasi | R&A provides CJB Reporting |
| **Plans / Pricing (Annual Plans)** | Jacquelyn Horgan | R&A provides AP take-rate, prospect-to-booking, 90d retention reporting |
| **Onboarding (OBX)** | Joshua Fischer | R&A surfaces activation funnel + DFY-OBX metrics |
| **Acquisition Agent** | (tentative, per WhatsApp thread 2026-03-20) | R&A provides training signals + outcome metrics |

---

## ESCALATE tier (out of R&A scope)

| Example | Why out of scope |
|---|---|
| Build MM multi-entity billing infra | Plans/PLC structural; not R&A |
| Launch Annual Plans rate-card experiment itself | Plans PM owns; R&A supports with reporting |
| Cross-Intuit QBO bundle | Intuit-wide GTM; Deepak not the DRI |
| Ramp down/up Analytics Agent GA scope | Deepak owns — but *scope changes* require SLT per G10 |
| Loyalty / UGC build | Ecomm-specific; partner/buy decision belongs to Ecomm leadership |
| HC allocation decisions | Engineering leadership |

---

## Success metrics for R&A + AI Agent surface

The agent should track R&A-specific metrics in addition to the headline Growth Tree:

| Metric | Canonical source | Backing query |
|---|---|---|
| Analytics Agent engagement rate | Amplitude / `product_health_weekly` derivations | Need query (gap) |
| Analytics Agent insights generated / week | Internal Project Alfred metric | Need pipe (gap) |
| Custom report creations / week | `bi_product.reporting_weekly_user_rollup` | `queries/30-reporting-weekly.sql` (to author) |
| HVC reporting VOC volume | last-stretch-voc-analyzer output | Direct pipe from existing agent |
| Revenue attribution coverage (% of C1 bookings with tracked source) | `bi_finance.daily_bookings.new_booking_timing` | `queries/11-ft-rolloff-bookings.sql` |
| Email Analytics page visits / C1 | Google Analytics internal | `queries/30-logins-weekly.sql` (proxy) |
| Dashboard load time / error rate | Splunk | Need pipe (gap) |

---

## Product accountability strategy document reference

See parent workspace: `/Users/dprabhakara/cursor/RA_PM_Accountability_527_Strategy.md` and `.pdf` for the broader R&A accountability context. This canon file is the agent's interpretation of that scope.
