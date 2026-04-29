-- description: Active + passive churn by account tenure bucket
-- backing_metric: Cohort churn × tenure
-- canon_ref: Churn Diagnostician
-- last_validated: 2026-04-28
-- params: @start_day DATE, @end_day DATE

SELECT
  account_tenure_months,
  SUM(active_churn_risk_users) AS active_churn_users,
  SUM(active_churn_risk_orders) AS active_churn_mrr,
  SUM(passive_billing_failure_churn_risk_users + passive_compliance_churn_risk_users) AS passive_churn_users,
  SUM(passive_billing_failure_churn_risk_orders + passive_compliance_churn_risk_orders) AS passive_churn_mrr,
  SUM(total_paid_users) AS total_paid_user_days,
  SAFE_DIVIDE(
    SUM(active_churn_risk_users + passive_billing_failure_churn_risk_users + passive_compliance_churn_risk_users),
    SUM(total_paid_users)
  ) AS daily_churn_rate_avg
FROM `mc-business-intelligence.bi_aggregate.churn_daily`
WHERE day BETWEEN @start_day AND @end_day
GROUP BY account_tenure_months
ORDER BY account_tenure_months
