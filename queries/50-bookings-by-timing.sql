-- description: New booking timing mix (immediate / direct / free-to-paid) for GTM lever analysis
-- backing_metric: Booking timing
-- canon_ref: GTM Lever Analyst
-- last_validated: 2026-04-28
-- params: @start_week DATE, @end_week DATE

SELECT
  week,
  new_booking_timing,
  package,
  SUM(total_bookings_users) AS bookings_users,
  SUM(total_bookings_order_amount) AS bookings_amount,
  SUM(self_serve_digital_bookings_users) AS self_serve_users,
  SUM(sales_bookings_users) AS sales_users,
  SUM(service_partners_bookings_users) AS service_partner_users,
  SUM(tech_partners_bookings_users) AS tech_partner_users
FROM `mc-business-intelligence.bi_aggregate.bookings_weekly`
WHERE week BETWEEN @start_week AND @end_week
  AND new_booking_timing IS NOT NULL
GROUP BY week, new_booking_timing, package
ORDER BY week DESC, new_booking_timing, package
