/* Write your PL/SQL query statement below */

select id 
from weather w
where temperature > (select temperature 
                     from weather we 
                     where we.recordDate = w.recordDate - 1)
