-- 대장균들의 자식의 수 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/299305

SELECT A.ID, COUNT(B.ID) AS CHILD_COUNT
FROM ECOLI_DATA AS A LEFT JOIN ECOLI_DATA AS B
ON A.ID = B.PARENT_ID
GROUP BY ID
ORDER BY A.ID ASC