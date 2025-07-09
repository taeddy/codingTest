-- 특정 형질을 가지는 대장균 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/301646

select count(*) as count
from ecoli_data
where (genotype & 2) = 0
    and ((genotype & 1 > 0) or (genotype & 4 > 0))