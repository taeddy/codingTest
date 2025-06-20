# 정원 (Easy)
# https://www.acmicpc.net/problem/24049
import itertools

N, M = map(int, input().split())
garden = [[0]]
flower_left = list(map(int, input().split()))
flower_up = list(map(int, input().split()))
garden[0] += flower_up

for f in flower_left:
    garden.append([f]+[0]*M)
# print(garden)

for i in range(1, N+1):
    for j in range(1, M+1):
        left, up = garden[i][j-1], garden[i-1][j]
        if left == up:
            garden[i][j] = 0
        else:
            garden[i][j] = 1

print(garden[-1][-1])