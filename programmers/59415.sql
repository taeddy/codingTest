-- 최댓값 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/59415

SELECT DATETIME '시간'
FROM ANIMAL_INS
WHERE DATETIME = (SELECT MAX(DATETIME) FROM ANIMAL_INS)
