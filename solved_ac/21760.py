# 야구 시즌
# https://www.acmicpc.net/problem/21760

# 풀이 포인트
# acc를 미리 계산해두는 식을 세우면 빠르게 연산이 가능하다.


def solution():
    T = int(input())
    for _ in range(T):
        N, M, k, D = map(int, input().split())
        # A, B가 있을때
        # total = kB * MC2 * N + B * NC2 * M^2
        B = 1
        last_total = 0
        acc = k * M * (M - 1) / 2 * N + N * (N - 1) / 2 * M * M
        B = D // acc
        print(int(acc * B)) if B else print(-1)


solution()
