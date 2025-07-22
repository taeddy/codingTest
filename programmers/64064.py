# 불량 사용자
# https://school.programmers.co.kr/learn/courses/30/lessons/64064
import re
from itertools import permutations

def solution(user_id, banned_id):
    answer_list = []
    for per in permutations(user_id, len(banned_id)):
        cnt = 0
        for idx, id in enumerate(per):
            ban = banned_id[idx].replace('*', '.')
            if re.match(ban, id) and len(id)==len(ban):
                cnt += 1
        if cnt == len(banned_id):
            per = sorted(per)
            if per not in answer_list:
                answer_list.append(per)

    return len(answer_list)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))