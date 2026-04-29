-- description: Bookings split by new_booking_timing (FT rolloff vs direct vs immediate)
-- backing_metric: Free Trial Rolloff Bookings, Existing Direct, New Direct
-- canon_ref: metrics-canon §Bookings
-- last_validated: 2026-04-28
-- params: @start_week DATE, @end_week DATE

SELECT
  week,
  new_booking_timing,
  SUM(total_bookings_users) AS bookings_users,
  SUM(total_bookings_order_amount) AS bookings_amount,
  SUM(total_bookings_users_prev_yr) AS bookings_users_prev_yr
FROM `mc-business-intelligence.bi_aggregate.bookings_weekly`
WHERE week BETWEEN @start_week AND @end_week
  AND new_booking_timing IS NOT NULL
GROUP BY week, new_booking_timing
ORDER BY week DESC, new_booking_timing
