-- 강원도에 위치한 생산공장 목록 출력하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131112

SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE SUBSTR(ADDRESS, 1, 2) = '강원'
