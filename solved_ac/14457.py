# Cow Tipping
# https://www.acmicpc.net/problem/14457

# 모든 소를 '0'으로 만드는 것이 목표

import itertools

N = int(input())

cows = []
for _ in range(N):
    cows.append(list(map(int, list(input()))))

def toggle(i, j):
    for x, y in itertools.product(range(i+1), range(j+1)):
        cows[x][y] = 1 - cows[x][y]

cnt = 0
for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if cows[i][j] == 1:
            toggle(i, j)
            cnt += 1

print(cnt)