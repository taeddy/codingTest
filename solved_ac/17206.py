# 준석이의 수학 숙제
# https://www.acmicpc.net/problem/17206

import sys

input = sys.stdin.readline

T = int(input())
Ns = list(map(int, input().split()))

li = {
    0: 0,
    1: 0,
    2: 0,
    3: 3,
    4: 3,
    5: 3,
    6: 9,
    7: 16,
    8: 16,
    9: 25,
    10: 25,
    11: 25,
    12: 37,
    13: 37,
    14: 51,
    15: 66,
    16: 66,
    17: 66,
    18: 84,
    19: 84,
    20: 84,
}

for N in Ns:
    share = N // 21
    rem = N % 21
    ans = 189 * share * (share + 1) / 2 + share * (105 - 189) + li[rem]
    print(int(ans))
