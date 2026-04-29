# Canon — ICP Definitions

> **Status:** Canonical. Agent reads, never writes.
> **Last updated:** 2026-04-28

Source: FY26 Strategic Narrative Exhibits 1, 2, 3, 5.

---

## Business size (revenue scope)

| Tier | Annual revenue | Notes |
|---|---|---|
| **Small** | <$2.5M | |
| **Lower Mid-Market** | $2.5M–$5M | |
| **Mid-Market** | $5M–$10M | FY26 MM scope tops out here |
| **Upper MM / Enterprise** | >$10M | Out of FY26 scope |

---

## Three priority ICPs (FY26)

### ICP 1 — Subscription-based MM

- **Target size:** Mid-Market (up to $10M revenue)
- **Verticals:** SaaS/Apps & Content (excludes ecomm and retail-services-with-subscription model)
- **Example businesses:** Project Management Software, Language Learning App, Audiobook Marketplace, Subscription Newsletters
- **Primary conversion goals:** Subscription, Subscription retention
- **Reasons to believe:** Scales quickly, overserved by enterprise tools, open to switch. Underindex market today: 6% of user base, 8% of revenue. Specialized needs (e.g., push) take time to develop, but core need overlap with Ecomm allows immediate benefits.
- **Value:** High
- **PMF:** Moderate
- **TAM (US):** 0.5M–1.2M
- **TAM growth:** >10%
- **MM TAM ($2.5M Biz Rev US):** ~30K
- **HV likelihood index:** 140 (SaaS 170)
- **Adv. Feature Usage index:** 120

### ICP 2 — Community-based Small/Lower-MM

- **Target size:** Small & Lower Mid-Market (up to $5M revenue)
- **Verticals:** Civic/Social & Institutions
- **Example businesses:** Museums, Community Development, Higher Ed/Universities, Charitable Foundations
- **Primary conversion goals:** Donation, Sign-up/Registration (incl. events)
- **Reasons to believe:** MM underserved by marketing tools in all-in-one biz solutions (e.g., donor platforms). Already 24% of user base, 21% of revenue. More likely to adopt MC advanced products. Opportunity to lean into email strength to capture more MM.
- **Value:** Moderate
- **PMF:** High
- **TAM (US):** 1.2M
- **TAM growth:** 3%
- **MM TAM:** 34K
- **HV likelihood index:** 130
- **MC penetration index (vs 3.2%):** 370 (highest of all targeted)
- **6mo new-user churn:** 41%

### ICP 3 — Digital sales-based Small/Lower-MM (Ecomm)

- **Target size:** Small & Lower Mid-Market (up to $5M revenue)
- **Verticals:** Ecommerce & Omnichannel Goods Sellers
- **Example businesses:** Apparel & Fashion, Kitchen & Dining, Personal Care Products
- **Primary conversion goals:** Purchase, Repeat Purchase (sometimes measured as GMV)
- **Reasons to believe:** Focus for past 4 years; more Ecomm integrations, automations, AI. 21% of user base, 25% of revenue. Extensive knowledge of Ecomm channels and industry; product opportunities/gaps clear. Halo effect for other SC verticals.
- **Value:** High
- **PMF:** Moderate
- **TAM (US):** 1.6M (Retail Trade) + 1.6M (All Other PBB)
- **TAM growth:** <0% (Retail Trade)
- **MM TAM:** 42K + 118K
- **HV likelihood index:** 130 (Retail Trade), 110 (All Other PBB)
- **6mo new-user churn:** 31% ECU (Ecomm Connected) / 43% non-ECU

---

## Deprioritized segments (FY26)

| Segment | Why deprioritized |
|---|---|
| Recreation | Low value, mid PMF |
| Hospitality | Medium value, mid PMF |
| Marketing Agencies | Medium value, mid PMF |
| Traditional Professional Services (Consulting, Legal, Graphic Designers, Accountants) | CC behavior — needs CRM hub before MC can deliver value. 1/3 use CRM as primary customer database. |
| Construction | CC behavior, low PMF (MC penetration index 20). |

---

## Decision-maker personas (MM)

- **Head of Marketing** — leading growth and retention
- **Head of Digital & Demand Generation** — owning email, automation, paid media

## Specialist (day-to-day user) personas (MM)

- **Growth & Performance Marketing Lead** — driving conversion and retention strategies
- **Lifecycle Marketing Lead** — managing audience lifecycle, automation, segmentation
- **Marketing & Revenue Operations Lead** — managing billing, reporting, ROI analytics

## Decision-maker personas (Ecomm Small/LMM)

- **Informed Founder** — primary decision-maker, often hands-on
- **Marketing Generalist** — wears many hats
- **Channel Specialist** — deep in 1-2 channels

---

## Package mapping

When `bi_aggregate.*.package` field is queried:

- **`Free`** — free tier (no MRR)
- **`Essentials`** — entry paid tier
- **`Standard`** — mid paid tier (where most experimentation happens)
- **`Premium`** — top paid tier (HVC concentration)
- **`<package_upgrade_plan>`** — package-plan ladder (specific to upgrade workflow)

---

## ICP filter heuristics for BigQuery

Until proper ICP joins exist in `bi_*` (likely via `bi_data_classified` or a yet-unbuilt ICP table), use these proxies:

| ICP | Proxy filter |
|---|---|
| **Subscription MM** | `package IN ('Standard', 'Premium')` AND `is_high_value = TRUE` AND `ecomm_status = 'Not Ecomm'` |
| **Community Small/LMM** | `package IN ('Essentials', 'Standard')` AND `ecomm_status = 'Not Ecomm'` AND industry-vertical=Civic/Nonprofit (requires industry classification join) |
| **Ecomm Small/LMM** | `ecomm_status IN ('Connected Ecomm', 'Likely Ecomm')` AND `is_high_value = FALSE OR list_size <= 25k` |

> ⚠️ These are PROXIES until a proper ICP table is built. Flag this gap in every analysis.
