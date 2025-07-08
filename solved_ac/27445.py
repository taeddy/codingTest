# Gorani Command
# https://www.acmicpc.net/problem/27445

def solution():
    N, M = map(int, input().split())
    left_dist = []
    for _ in range(N-1):
        left_dist.append(int(input()))
    bottom_dist = list(map(int, input().split()))
    left_dist.append(bottom_dist[0])

    _idx_1 = left_dist.index(min(left_dist)) + 1
    _idx_2 = bottom_dist.index(min(bottom_dist)) + 1

    print(_idx_1, _idx_2)

solution()