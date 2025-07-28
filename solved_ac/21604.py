# 겹강 찾기
# https://www.acmicpc.net/problem/21604

# 한 개의 수업을 함께 수업을 듣는 사람이 한 쌍도 없었습니다 >>>>        N >= M
# K <= M
# 단, 싸이컴회원+상상친구 중 분반이 겹치는 인원이 있어서는 안됨.

import itertools
import random

def count_same_elements(l1, l2):
    cnt = 0
    for e1, e2 in zip(l1, l2):
        if e1 == e2:
            cnt += 1
    return cnt

def can_be_added(new, imaginary_friends):
    for old in imaginary_friends:
        cnt = count_same_elements(new, old)
        if cnt > 0:
            return False
    return True

# 입력 처리
N, M = map(int, input().split())
classes = [list(map(int, input().split())) for _ in range(M)]

# 분반 정보를 string으로 저장 (비교를 편리하게 만듦)
division_dict = []
for _class in classes:
    division_dict.append(''.join(map(str, _class)))

imaginary_friends = []
# 상상 친구 생성
while True:
    imaginary_friends = []
    friends = list(itertools.product(range(1, N+1), repeat=N))
    while True:
        friend = random.choice(friends)
        if len(imaginary_friends) == M:
            break
        joined = ''.join(map(str, friend))
        if joined not in division_dict and can_be_added(friend, imaginary_friends):
            imaginary_friends.append(friend)
            
    if len(imaginary_friends) == M:
        break

# 출력
print(len(imaginary_friends))
for friend in imaginary_friends:
    print(' '.join(map(str, friend)))
