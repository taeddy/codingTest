# 알고리즘 수업 - 선택 알고리즘 1
# https://www.acmicpc.net/problem/24398

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, Q, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

def swap(a, b):
    global cnt
    cnt += 1
    if cnt == K: print(min(a, b), max(a, b))
    return b, a

def select(p, r, q):
    if p == r: return A[p]
    t = partition(p, r)
    k = t - p + 1
    if q < k: return select(p, t-1, q)
    elif q == k: return A[t]
    else: return select(t+1, r, q-k)

def partition(p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = swap(A[i], A[j])
    if i+1 != r:
        A[i+1], A[r] = swap(A[i+1], A[r])
    return i+1

select(0, N-1, Q)
if cnt < K:
    print(-1)
