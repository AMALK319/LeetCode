/* Write your PL/SQL query statement below */

select a1.player_id , to_char(min(a1.event_date), 'YYYY-mm-dd') as first_login
from Activity a1
group by a1.player_id