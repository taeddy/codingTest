# Trapped in the Haybales
# https://www.acmicpc.net/problem/10766

import sys
input = sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
    li.append(tuple(map(int, input().split())))
li.sort(key=lambda x: x[1])

ans = 0
for i in range(N-1):
    left = i
    right = i+1
    sig = False
    while True:
        if left == -1 or right == N:
            sig = True
            break
        dist = li[right][1] - li[left][1]
        if dist <= li[left][0] and dist <= li[right][0]:
            break
        if dist > li[right][0]:
            right += 1
        if dist > li[left][0]:
            left -= 1
    if not sig:
        ans += li[i + 1][1] - li[i][1]

print(ans)
