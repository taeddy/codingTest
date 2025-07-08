# 배찬우는 배열을 좋아해
# https://www.acmicpc.net/problem/25966

# 풀이 포인트
# input대신 stdin.readline 사용하기

from sys import stdin
input = stdin.readline

def solution():
    N, M, q = map(int, input().split())

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    # k: v = 실제 idx: 메모리 상 idx
    mapping = {i: i for i in range(N)}

    for _ in range(q):
        line = list(map(int, input().split()))
        if line[0]:
            i, j = mapping[line[1]], mapping[line[2]]
            mapping[i], mapping[j] = mapping[j], mapping[i]
        else:
            i, j, k = mapping[line[1]], mapping[line[2]], line[3]
            matrix[i][j] = k
            
    [print(*matrix[i[1]]) for i in sorted(mapping.items())]

solution()
