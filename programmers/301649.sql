-- 대장균의 크기에 따라 분류하기 2
-- https://school.programmers.co.kr/learn/courses/30/lessons/301649

SELECT A.ID,
    CASE
        WHEN A.PER <= 0.25 THEN 'CRITICAL'
        WHEN A.PER <= 0.5 THEN 'HIGH'
        WHEN A.PER <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM (
    SELECT ID, PERCENT_RANK() OVER(ORDER BY SIZE_OF_COLONY DESC) AS PER
    FROM ECOLI_DATA
) AS A
ORDER BY A.ID ASC