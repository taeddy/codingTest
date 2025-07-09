-- 재구매가 일어난 상품과 회원 리스트 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131536

select a.USER_ID, a.PRODUCT_ID
from ONLINE_SALE as a
group by user_id, product_id
having count(*) > 1
ORDER BY a.USER_ID ASC, a.PRODUCT_ID DESC