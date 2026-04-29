-- description: Weekly active + passive churn (users + MRR)
-- backing_metric: Active/Passive Churn Users + $
-- canon_ref: metrics-canon §Churn
-- last_validated: 2026-04-28
-- params: @start_day DATE, @end_day DATE

SELECT
  DATE_TRUNC(day, WEEK(MONDAY)) AS week,
  SUM(active_churn_risk_users) AS active_churn_users,
  SUM(active_churn_risk_orders) AS active_churn_mrr,
  SUM(passive_billing_failure_churn_risk_users) AS passive_billing_users,
  SUM(passive_billing_failure_churn_risk_orders) AS passive_billing_mrr,
  SUM(passive_compliance_churn_risk_users) AS passive_compliance_users,
  SUM(passive_compliance_churn_risk_orders) AS passive_compliance_mrr,
  SUM(active_churn_risk_users + passive_billing_failure_churn_risk_users + passive_compliance_churn_risk_users) AS total_churn_users,
  SUM(active_churn_risk_orders + passive_billing_failure_churn_risk_orders + passive_compliance_churn_risk_orders) AS total_churn_mrr,
  AVG(total_paid_users) AS avg_total_paid_users
FROM `mc-business-intelligence.bi_aggregate.churn_daily`
WHERE day BETWEEN @start_day AND @end_day
GROUP BY week
ORDER BY week DESC
