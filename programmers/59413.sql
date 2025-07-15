-- 입양 시각 구하기(2)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59413

SET @HOUR = -1;
SELECT (@HOUR := @HOUR + 1) HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR) COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23;
