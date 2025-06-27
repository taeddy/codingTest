# 행렬 제곱
# https://www.acmicpc.net/problem/10830


def dot(vec1, vec2):
    return sum([v1 * v2 for v1, v2 in zip(vec1, vec2)]) % 1000


def matrix_multiplication(matA, matB):
    N = len(matA)
    res = []
    matB_trans = list(zip(*matB))

    for row in range(N):
        tmp = []
        for col in range(N):
            tmp.append(dot(matA[row], matB_trans[col]))
        res.append(tmp)
    return res


def matrix_powered(mat, power):
    if power == 1:
        return mat
    elif power == 2:
        return matrix_multiplication(mat, mat)

    r, c = power // 2, power % 2
    mat_half = matrix_powered(mat, r)
    res = matrix_multiplication(mat_half, mat_half)
    if c:  # 홀수
        res = matrix_multiplication(res, mat)
    return res


N, B = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

# Time Over
# res = mat.copy()
# for _ in range(B - 1):
#     res = matrix_multiplation(res, mat)

res = matrix_powered(mat, B)

# print answer
for row in range(N):
    for col in range(N):
        print(res[row][col] % 1000, end=" ")
    print()
