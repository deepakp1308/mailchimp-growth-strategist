-- description: Weekly total new bookings (count + revenue)
-- backing_metric: Total New Bookings + revenue
-- canon_ref: metrics-canon §Bookings
-- last_validated: 2026-04-28
-- params: @start_week DATE, @end_week DATE

SELECT
  week,
  SUM(total_bookings_users) AS total_bookings_users,
  SUM(total_bookings_order_amount) AS total_bookings_order_amount,
  SUM(self_serve_digital_bookings_users) AS self_serve_users,
  SUM(self_serve_digital_bookings_order_amount) AS self_serve_amount,
  SUM(sales_bookings_users) AS sales_users,
  SUM(sales_bookings_order_amount) AS sales_amount,
  SUM(service_partners_bookings_users) AS service_partner_users,
  SUM(tech_partners_bookings_users) AS tech_partner_users,
  SUM(total_bookings_users_prev_yr) AS total_bookings_users_prev_yr,
  SUM(total_bookings_order_amount_prev_yr) AS total_bookings_order_amount_prev_yr
FROM `mc-business-intelligence.bi_aggregate.bookings_weekly`
WHERE week BETWEEN @start_week AND @end_week
GROUP BY week
ORDER BY week DESC
