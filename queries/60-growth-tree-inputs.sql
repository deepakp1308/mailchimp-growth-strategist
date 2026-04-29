-- description: All inputs to the $50M Growth Tree decomposition
-- backing_metric: Paid Users, ARPU, Churn rate, Activation rate, Booking timing mix
-- canon_ref: mc-growth-tree-50m
-- last_validated: 2026-04-28
-- params: @start_week DATE, @end_week DATE
-- NOTE: This is a multi-CTE summary query. Heavy. Cache and reuse.

WITH ph AS (
  SELECT
    week,
    SUM(activations) AS activations,
    SUM(logins) AS logins,
    SUM(email_creates) AS email_creates,
    SUM(first_time_sends) AS first_time_sends,
    SUM(new_bookings) AS new_bookings_count,
    SUM(sms_paid_plan_users) AS sms_paid_plan_users
  FROM `mc-business-intelligence.bi_aggregate.product_health_weekly`
  WHERE week BETWEEN @start_week AND @end_week
  GROUP BY week
),
bk AS (
  SELECT
    week,
    SUM(total_bookings_users) AS total_bookings_users,
    SUM(total_bookings_order_amount) AS total_bookings_order_amount
  FROM `mc-business-intelligence.bi_aggregate.bookings_weekly`
  WHERE week BETWEEN @start_week AND @end_week
  GROUP BY week
),
ch AS (
  SELECT
    DATE_TRUNC(day, WEEK(MONDAY)) AS week,
    SUM(active_churn_risk_users) AS active_churn_users,
    SUM(active_churn_risk_orders) AS active_churn_mrr,
    SUM(passive_billing_failure_churn_risk_users + passive_compliance_churn_risk_users) AS passive_churn_users,
    SUM(passive_billing_failure_churn_risk_orders + passive_compliance_churn_risk_orders) AS passive_churn_mrr,
    AVG(total_paid_users) AS avg_total_paid_users,
    AVG(total_order_amount) AS avg_total_order_amount
  FROM `mc-business-intelligence.bi_aggregate.churn_daily`
  WHERE day BETWEEN DATE_SUB(@start_week, INTERVAL 0 DAY) AND DATE_ADD(@end_week, INTERVAL 6 DAY)
  GROUP BY week
)
SELECT
  ph.week,
  ph.activations,
  ph.logins,
  ph.email_creates,
  ph.first_time_sends,
  ph.new_bookings_count,
  ph.sms_paid_plan_users,
  bk.total_bookings_users,
  bk.total_bookings_order_amount,
  ch.active_churn_users,
  ch.active_churn_mrr,
  ch.passive_churn_users,
  ch.passive_churn_mrr,
  ch.avg_total_paid_users,
  ch.avg_total_order_amount,
  SAFE_DIVIDE(bk.total_bookings_order_amount, bk.total_bookings_users) AS arpu_per_booking,
  SAFE_DIVIDE(ch.avg_total_order_amount, ch.avg_total_paid_users) AS arpu_per_paid_user,
  SAFE_DIVIDE(ch.active_churn_users + ch.passive_churn_users, ch.avg_total_paid_users) AS weekly_total_churn_rate,
  SAFE_DIVIDE(ch.active_churn_users, ch.avg_total_paid_users) AS weekly_active_churn_rate,
  SAFE_DIVIDE(ch.passive_churn_users, ch.avg_total_paid_users) AS weekly_passive_churn_rate
FROM ph
LEFT JOIN bk USING (week)
LEFT JOIN ch USING (week)
ORDER BY ph.week DESC
