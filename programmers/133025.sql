-- 과일로 만든 아이스크림 고르기
-- https://school.programmers.co.kr/learn/courses/30/lessons/133025

select a.FLAVOR
from FIRST_HALF as A join ICECREAM_INFO as b
on A.FLAVOR = B.FLAVOR
where a.total_order >= 3000 and b.ingredient_type = 'fruit_based'
order by a.total_order desc