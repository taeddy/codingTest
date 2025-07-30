# 알고리즘 수업 - 선택 알고리즘 1
# https://www.acmicpc.net/problem/24398

# 코딩 알고리즘 문제 풀이에서 python이 실행시간이 길다는 점과, pypy3을 이용하더라도 메모리를 많이 차지한다는 불리함이 있다.
# 문제에 제시된 의사코드를 그대로 구현하면 풀이가 가능한 타 언어와 비교하여 풀이가 일관되지 않으므로 C++을 이용하여 1차적으로 해결함.

import sys
sys.setrecursionlimit(10**9)

N, Q, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

def select(p, r, q):
    if p == r: return A[p]
    t = partition(p, r)
    k = t - p + 1
    if q < k: return select(p, t-1, q)
    elif q == k: return A[t]
    else: return select(t+1, r, q-k)

def partition(p, r):
    global cnt
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            A[i+1], A[j] = A[j], A[i+1]
            cnt += 1
            if cnt == K:
                print(A[i+1], A[j])
                exit()
            i += 1
    if i+1 != r:
        A[i+1], A[r] = A[r], A[i+1]
        cnt += 1
        if cnt == K:
            print(A[i+1], A[j])
            exit()
    return i+1

select(0, N-1, Q)
if cnt < K:
    print(-1)
