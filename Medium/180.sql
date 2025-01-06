select distinct l1.num as ConsecutiveNums
from logs l1
join logs l2 on l1.id=l2.id-1
join logs l3 on l2.id=l3.id-1
where l1.num=l2.num and l2.num=l3.num;

SELECT DISTINCT l1.num AS ConsecutiveNums
FROM logs l1, logs l2, logs l3
WHERE l2.id = l1.id + 1 AND l3.id = l1.id + 2 AND l1.num = l2.num AND l1.num = l3.num;