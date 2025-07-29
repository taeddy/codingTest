# 겹강 찾기
# https://www.acmicpc.net/problem/21604

# 이미 짜여진 회원의 커리큘럼과 같은 N*M을 만들고, 각 열을 rotate하면 됨.

def solve():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]

    # 가상 친구 수는 M명
    print(M)
    # B[i][j] = A[(i + j) % M][j]
    for i in range(M):
        row = []
        for j in range(N):
            row.append(A[(i + j) % M][j])
        print(*row)

if __name__ == "__main__":
    solve()
