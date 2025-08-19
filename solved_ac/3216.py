# 다운로드
# https://www.acmicpc.net/problem/3216

import sys
input = sys.stdin.readline

N = int(input())

res = 0
wait = 0
for _ in range(N):
    D, V = map(int, input().split())

    if res < V:
        wait += V - res
        res = D
    elif res >= V:
        res = res - V + D

print(wait)