# 가변 배열
# https://www.acmicpc.net/problem/29729

import sys
input = sys.stdin.readline

S, N, M = map(int, input().split())
now = 0

for _ in range(N+M):
    re = int(input())
    if re:
        now += 1
        if now > S:
            S *= 2
    else:
        now -= 1

print(S)
        
