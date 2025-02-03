select a.Score as score , 
    (select count(distinct Score) from Scores where Score >= a.Score) as "rank"
from Scores a
order by a.Score desc