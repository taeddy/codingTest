-- 한 해에 잡은 물고기 수 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/298516

SELECT COUNT(*) FISH_COUNT
FROM FISH_INFO
WHERE SUBSTR(TIME, 1, 4) = '2021'
