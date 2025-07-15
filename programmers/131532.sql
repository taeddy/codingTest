-- 년, 월, 성별 별 상품 구매 회원 수 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131532

-- '연, 월, 성별 별로 상품을 구매한 회원수' 라는 말로부터...
-- 같은 연, 월에 특정 회원이 여러 번 구매했다면 (day가 다른 경우) 회원ID가 중복되니까 distinct로 제거

SELECT YEAR(OS.SALES_DATE) YEAR, MONTH(OS.SALES_DATE) MONTH, GENDER, COUNT(DISTINCT OS.USER_ID) USERS
FROM USER_INFO UI
JOIN ONLINE_SALE OS ON UI.USER_ID = OS.USER_ID
WHERE UI.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER
