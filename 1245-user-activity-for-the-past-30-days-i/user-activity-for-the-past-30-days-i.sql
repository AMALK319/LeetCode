/* Write your PL/SQL query statement below */
SELECT TO_CHAR(activity_date, 'YYYY-MM-DD') as day, COUNT(DISTINCT user_id) as active_users
FROM activity
WHERE activity_date <= TO_DATE('2019-07-27', 'YYYY-MM-DD') 
  AND activity_date > TO_DATE('2019-07-27', 'YYYY-MM-DD') - 30
GROUP BY activity_date
