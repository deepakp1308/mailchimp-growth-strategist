# Canon — Metrics & BigQuery Mapping

> **Status:** Canonical — agent reads, never writes. Only Deepak edits.
> **Last updated:** 2026-04-28

This file is the **single source of truth** for metric definitions. Every metric mentioned in any analysis must be traceable back to a row here.

When in doubt: **BigQuery is canon. Tableau and Slack-quoted numbers are reference points.** Discrepancies log in `contradictions.md`.

---

## Primary aggregate tables

### `mc-business-intelligence.bi_aggregate.product_health_weekly`
**Description:** Aggregated weekly Product Health table with all metrics and slices. Backs the *Mailchimp Product Health Dashboard — Executive Overview*.
**Partition:** `week` (DATE), Monday-aligned.
**Cluster:** `agg_key`, `fy_number`, `shard`.
**Dimensions:** `ecomm_status`, `is_high_value`, `package`, `list_size`, `shard`.

### `mc-business-intelligence.bi_aggregate.bookings_weekly`
**Description:** Aggregated weekly Bookings table.
**Partition:** `week`.
**Dimensions:** `country_group`, `ecomm_status`, `is_high_value`, `package`, `account_tenure_months`, `new_booking_tenure_months`, `new_booking_timing`, `list_size`.

### `mc-business-intelligence.bi_aggregate.churn_daily`
**Description:** Aggregated daily Churn view.
**Partition:** `day`.
**Dimensions:** `country_group`, `ecomm_status`, `is_high_value`, `package`, `account_tenure_months`, `new_booking_tenure_months`, `new_booking_timing`, `list_size`.

### `mc-business-intelligence.bi_aggregate.customer_engagements_weekly`
**Description:** Live channels (zoom calls, webinars, office hours) — touchpoint tracking.

### `mc-business-intelligence.bi_aggregate.free_trials_weekly`
**Description:** Free trials with cohort retention (1/2/3/6/12/24 month).

---

## Headline metric definitions (mapped to dashboard)

### Activation & WAU

| Metric | Definition | BigQuery field | Source query |
|---|---|---|---|
| **Total Paid in Current Week** | Count of users with positive order amount in week | derived from `bi_temp.bi_temp_paid_users_daily_rollup` | `queries/01-paid-users-current-week.sql` |
| **Paid WAU** | Active paid users in week (engagement-based) | `bi_aggregate.product_health_weekly.logins` filtered to paid + active criteria | `queries/02-paid-wau.sql` |
| **Free WAU** | Active free users in week | same table, free filter | `queries/03-free-wau.sql` |
| **New Activations in Week** | New users who confirmed email (account activated) | `product_health_weekly.activations` | `queries/04-activations-weekly.sql` |
| **Paid WAU Rate** | Paid WAU / Total Paid | derived | `queries/05-paid-wau-rate.sql` |
| **Free WAU Rate** | Free WAU / Total Free | derived | `queries/06-free-wau-rate.sql` |

### Bookings

| Metric | Definition | BigQuery field | Source query |
|---|---|---|---|
| **Total New Bookings** | First monthly marketing plan purchases (paid) | `product_health_weekly.new_bookings` and `bookings_weekly.total_bookings_users` | `queries/10-new-bookings-weekly.sql` |
| **Free Trial Rolloff Bookings** | New bookings from free-trial conversion | `bookings_weekly` filtered to `new_booking_timing = 'free to paid'` | `queries/11-ft-rolloff-bookings.sql` |
| **Existing Users Direct Bookings** | New bookings from `direct to paid` (within 30d of signup) | `bookings_weekly` filtered to `direct to paid` | `queries/12-existing-direct-bookings.sql` |
| **New Users Direct Bookings** | `immediate to paid` — bookings in first 30 days | `bookings_weekly` filtered to `immediate to paid` | `queries/13-new-direct-bookings.sql` |
| **Essentials/Standard/Premium Bookings** | Tier mix | `bookings_weekly` × `package` dimension | `queries/14-bookings-by-tier.sql` |

### Churn (active vs. passive)

| Metric | Definition | BigQuery field | Source query |
|---|---|---|---|
| **Active Churn Users (weekly)** | Users with active initial churn activity (closed, downgrade, paused, cancel CC, switch to payg, chargeback) | `churn_daily.active_churn_risk_users` summed week | `queries/20-active-churn-weekly.sql` |
| **Passive Churn Users (weekly)** | Users with passive churn (billing failure + compliance) | `passive_billing_failure_churn_risk_users + passive_compliance_churn_risk_users` | `queries/21-passive-churn-weekly.sql` |
| **Active Churn $ (MRR)** | Previous-month MRR of users at risk of active churn | `churn_daily.active_churn_risk_orders` | `queries/22-active-churn-mrr.sql` |
| **Passive Churn $ (MRR)** | Previous-month MRR of users at risk of passive churn | sum of two passive-orders fields | `queries/23-passive-churn-mrr.sql` |
| **Active Churn Rate (weekly)** | active_churn_users / total_paid | derived | `queries/24-active-churn-rate.sql` |
| **Passive Churn Rate (weekly)** | passive_churn_users / total_paid | derived | `queries/25-passive-churn-rate.sql` |
| **Total Churn Rate (weekly)** | (active + passive) / total_paid | derived | `queries/26-total-churn-rate.sql` |
| **Active Churn Share** | active / (active + passive) | derived | `queries/27-active-churn-share.sql` |
| **Passive Churn Share** | passive / (active + passive) | derived | `queries/28-passive-churn-share.sql` |

> **WARNING:** active and passive churn use the same denominator (total_paid_users) but very different numerators. The PDF dashboard's "Total Churn Rate" sums both. **Do not** silently use one as a substitute for the other.

### Product engagement

| Metric | Definition | BigQuery field | Source query |
|---|---|---|---|
| **Logged In Users (weekly)** | Total user logins | `product_health_weekly.logins` | `queries/30-logins-weekly.sql` |
| **Email Creates** | User email creations | `product_health_weekly.email_creates` | `queries/31-email-creates.sql` |
| **First-Time Sends** | Users sending email for first time | `product_health_weekly.first_time_sends` | `queries/32-first-time-sends.sql` |
| **Email Sends** | Total email sends | `product_health_weekly.email_sends` | `queries/33-email-sends.sql` |
| **Email Payload Sent** | Bulk email sends qualifying for payload metric | `product_health_weekly.email_payload_sent` | `queries/34-email-payload.sql` |
| **CJB Creates / Starts** | Customer Journey Builder | derived from journey events (separate dataset) | `queries/35-cjb-metrics.sql` |
| **SMS Creates / Publishes / Sends** | SMS campaign + journey | `product_health_weekly.sms_campaign_creates`, `sms_campaign_sends`, `sms_first_time_campaign_sends`, `sms_cjb_sends`, `sms_cjb_keywords_created`, `sms_paid_plan_users` | `queries/36-sms-metrics.sql` |
| **Feature Payoffs** | Composite of qualifying activation events per user | `bi_product.prod_payoff_daily_status` rolled to week | `queries/37-feature-payoffs.sql` |

### Year-over-year & rates

Every metric in `product_health_weekly` and `bookings_weekly` has a `_prev_yr` companion (LAG of same metric exactly 1 year prior, allowing YoY% calc). Use these for the dashboard's `PY` (Prior Year) column.

For `ITPY` (Index to Prior Year):

```
ITPY = round(100 * current / prev_yr, 0)
```

---

## Targets tables

| Table | Use |
|---|---|
| `bi_finance.new_bookings_targets` | Target curves for new bookings — used by Strategy Reconciler |
| `bi_finance.paid_users_targets` | Target curves for paid user count |
| `bi_finance.net_order_value_targets` | Net order value targets |
| `bi_aggregate.mbr_targets_monthly` | MBR (Monthly Business Review) target alignment |

---

## Filter dimensions (used by all rollups)

| Dimension | Values |
|---|---|
| `ecomm_status` | `Connected Ecomm` / `Likely Ecomm` / `Not Ecomm` |
| `is_high_value` | `TRUE` / `FALSE` (HVC flag) |
| `package` | `Free` / `Essentials` / `Standard` / `Premium` / `<package_upgrade_plan>` |
| `account_tenure_months` | `<1` / `<3` / `<6` / `<12` / `<24` / `24+` |
| `new_booking_tenure_months` | same buckets |
| `new_booking_timing` | `immediate to paid` / `direct to paid` / `free to paid` |
| `list_size` | bucket ranges (subscribed + unsubscribed + transactional) |
| `country_group` | analytics-defined regional groupings |

---

## Cross-checks (data quality reminders)

- **SMS data was missing from 2024-12-15 to 2025-01-19** — DE was working on backfill (per dashboard footnote). Verify before quoting that period.
- **`product_reporting_production_table`** in `bi_product` is a Tableau-feeder table. Don't use it as primary source — go to `product_health_weekly`.
- **Tableau dashboards have ~24h-72h lag** vs. BigQuery actuals.
- **`% Churn Overview.xlsx`** is a Finance-curated artifact — when it disagrees with `churn_daily`, log in `contradictions.md`. Finance source has known sign-off; BigQuery has known recency.
