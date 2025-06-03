/* Write your PL/SQL query statement below */
select r.contest_id, Round(
    (
        (count(r.user_id)*100)/(select count(distinct user_id) from users)
    )
    ,2) as percentage
from Register r

group by r.contest_id
order by percentage desc, r.contest_id asc
