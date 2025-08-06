# 준석이의 수학 숙제
# https://www.acmicpc.net/problem/17206

import sys

input = sys.stdin.readline

T = int(input())
Ns = list(map(int, input().split()))


def cal_sum(n, x):
    return n * (n + 1) // 2 * x


for N in Ns:
    ans = cal_sum(N // 3, 3) + cal_sum(N // 7, 7) - cal_sum(N // 21, 21)
    print(ans)
