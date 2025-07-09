-- 조건에 부합하는 중고거래 댓글 조회하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/164673

select a.TITLE, a.BOARD_ID , b.REPLY_ID, b.WRITER_ID, b.CONTENTS, DATE_FORMAT(b.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from used_goods_board as a inner join used_goods_reply as b
on a.board_id = b.board_id
where substr(a.created_date, 1, 7) = '2022-10'
order by b.created_date ASC, a.TITLE ASC