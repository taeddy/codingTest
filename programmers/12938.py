# 최고의 집합
# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if n > s:
        return [-1]
    n_normal = s//n
    n_p1_cnt = s%n
    n_p1 = s//n+1
    answer = [n_normal]*(n-n_p1_cnt) + [n_p1]*n_p1_cnt

    return answer

# testcases = [[2, 9, [4, 5]], [2, 1, [-1]], [2, 8, [4, 4]]]
# print(solution(2, 8))