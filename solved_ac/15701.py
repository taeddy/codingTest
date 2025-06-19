# 순서쌍
# https://www.acmicpc.net/problem/15701

import math

N = int(input())

cnt = 0
for i in range(1, math.trunc(math.sqrt(N))+1):
    if N % i != 0:
        continue
    if N//i != i:
        cnt += 2
    else:
        cnt += 1
print(cnt)