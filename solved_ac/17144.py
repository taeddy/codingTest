# 입력
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 찾기
air_cleaner = []
for i in range(R):
    if board[i][0] == -1:
        air_cleaner.append(i)

# 방향: 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def spread_dust():
    new_board = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                spread_amount = board[r][c] // 5
                count = 0
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
                        new_board[nr][nc] += spread_amount
                        count += 1
                board[r][c] -= spread_amount * count
    for r in range(R):
        for c in range(C):
            board[r][c] += new_board[r][c]


def clean_air():
    top = air_cleaner[0]
    bottom = air_cleaner[1]

    # 위쪽 반시계
    for i in range(top - 1, 0, -1):
        board[i][0] = board[i - 1][0]
    for i in range(C - 1):
        board[0][i] = board[0][i + 1]
    for i in range(top):
        board[i][C - 1] = board[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        board[top][i] = board[top][i - 1]
    board[top][1] = 0

    # 아래쪽 시계
    for i in range(bottom + 1, R - 1):
        board[i][0] = board[i + 1][0]
    for i in range(C - 1):
        board[R - 1][i] = board[R - 1][i + 1]
    for i in range(R - 1, bottom, -1):
        board[i][C - 1] = board[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        board[bottom][i] = board[bottom][i - 1]
    board[bottom][1] = 0


# T초 동안 반복
for _ in range(T):
    spread_dust()
    clean_air()

# 결과 합산
answer = 0
for r in range(R):
    for c in range(C):
        if board[r][c] > 0:
            answer += board[r][c]
print(answer)
