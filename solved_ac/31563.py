# 수열 회전과 쿼리
# https://www.acmicpc.net/problem/31563
import sys
N, Q = map(int, input().split())
A = list(map(int, input().split()))*2
acc = [0]
for a in A:
    acc.append(acc[-1]+a)

start_idx = 0
for _ in range(Q):
    line = list(map(int, sys.stdin.readline().split()))
    if line[0] == 3:
        a = (line[1]-1+start_idx)%N
        print(acc[a+line[2]-line[1]+1]-acc[a])
    else:
        start_idx += (-1)**line[0]*line[1]
