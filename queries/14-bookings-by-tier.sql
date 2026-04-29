-- description: Tier-level bookings mix (Essentials/Standard/Premium)
-- backing_metric: Tier mix (Bookings)
-- canon_ref: metrics-canon §Bookings
-- last_validated: 2026-04-28
-- params: @start_week DATE, @end_week DATE

SELECT
  week,
  package,
  SUM(total_bookings_users) AS bookings_users,
  SUM(total_bookings_order_amount) AS bookings_amount,
  SUM(total_bookings_users_prev_yr) AS bookings_users_prev_yr,
  SUM(total_bookings_order_amount_prev_yr) AS bookings_amount_prev_yr
FROM `mc-business-intelligence.bi_aggregate.bookings_weekly`
WHERE week BETWEEN @start_week AND @end_week
GROUP BY week, package
ORDER BY week DESC, package
