-- 가장 비싼 상품 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131697

SELECT PRICE
FROM PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM PRODUCT)
