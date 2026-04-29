# BigQuery query templates

Each `.sql` file is a versioned, parameterized query. The `mc-bigquery-runner` subagent runs these and caches results to `knowledge/bigquery/<query-name>__<run_ts>.json`.

## Conventions

- Every query starts with a header comment: `-- description`, `-- backing_metric`, `-- canon_ref`, `-- last_validated`.
- Parameters are SQL `@params` style — passed by the runner.
- Date filtering uses partition fields when available (`week`, `day`).
- `LIMIT` is set explicitly to bound costs.
- All metric columns get aliased with the canon name from `canon/metrics-canon.md`.

## Index

| File | Metric | Canon ref |
|---|---|---|
| `01-paid-users-current-week.sql` | Total Paid in Current Week | metrics-canon §Activation |
| `04-activations-weekly.sql` | New Activations | metrics-canon §Activation |
| `10-new-bookings-weekly.sql` | Total New Bookings | metrics-canon §Bookings |
| `11-ft-rolloff-bookings.sql` | Free Trial Rolloff | metrics-canon §Bookings |
| `14-bookings-by-tier.sql` | Tier mix | metrics-canon §Bookings |
| `20-active-churn-weekly.sql` | Active Churn (users) | metrics-canon §Churn |
| `21-passive-churn-weekly.sql` | Passive Churn (users) | metrics-canon §Churn |
| `22-active-churn-mrr.sql` | Active Churn $ | metrics-canon §Churn |
| `26-total-churn-rate.sql` | Total Churn Rate | metrics-canon §Churn |
| `30-logins-weekly.sql` | Logins | metrics-canon §Engagement |
| `31-email-creates.sql` | Email Creates | metrics-canon §Engagement |
| `36-sms-metrics.sql` | SMS bundle | metrics-canon §Engagement |
| `40-cohort-churn-by-package.sql` | Cohort churn slice | Churn Diagnostician |
| `41-cohort-churn-by-tenure.sql` | Cohort churn × tenure | Churn Diagnostician |
| `50-bookings-by-timing.sql` | New booking timing mix | GTM Lever Analyst |
| `60-growth-tree-inputs.sql` | All inputs to Growth Tree | mc-growth-tree-50m |
