# Hour for a Run
# https://www.acmicpc.net/problem/17536

import math


def solution():
    V, N = map(int, input().split())
    _1lap = V * N / 10
    for i in range(1, 10):
        print(math.ceil(i * _1lap), end=' ')


solution()
