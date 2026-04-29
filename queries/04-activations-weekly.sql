-- description: Weekly new-user activations (signups + email-confirmed)
-- backing_metric: New Activations in Week
-- canon_ref: metrics-canon §Activation
-- last_validated: 2026-04-28
-- params: @start_week DATE, @end_week DATE

SELECT
  week,
  SUM(activations) AS activations,
  SUM(activations_prev_yr) AS activations_prev_yr,
  SAFE_DIVIDE(SUM(activations), SUM(activations_prev_yr)) AS yoy_ratio
FROM `mc-business-intelligence.bi_aggregate.product_health_weekly`
WHERE week BETWEEN @start_week AND @end_week
GROUP BY week
ORDER BY week DESC
