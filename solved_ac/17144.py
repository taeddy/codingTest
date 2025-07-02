# 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
air_cleaner = []
for i in range(R):
    if board[i][0] == -1:
        air_cleaner.append(i)
        air_cleaner.append(i + 1)
        break


def spread_dust():
    new_board = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                spread_amount = board[i][j] // 5
                spread_count = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        new_board[nx][ny] += spread_amount
                        spread_count += 1
                new_board[i][j] -= spread_amount * spread_count
    for i in range(R):
        for j in range(C):
            board[i][j] += new_board[i][j]


def clean_dust():
    top = air_cleaner[0]
    bottom = air_cleaner[1]
    # 위쪽 반시계
    ## 왼쪽
    for row in range(top - 1, 0, -1):
        board[row][0] = board[row - 1][0]
    ## 위
    for col in range(C - 1):
        board[0][col] = board[0][col + 1]
    ## 오른쪽
    for row in range(top):
        board[row][C - 1] = board[row + 1][C - 1]
    ## 아래
    for col in range(C - 1, 1, -1):
        board[top][col] = board[top][col - 1]
    board[top][1] = 0

    # 아래쪽 시계
    ## 왼쪽
    for row in range(bottom + 1, R - 1):
        board[row][0] = board[row + 1][0]
    ## 아래
    for col in range(C - 1):
        board[R - 1][col] = board[R - 1][col + 1]
    ## 오른쪽
    for row in range(R - 1, bottom, -1):
        board[row][C - 1] = board[row - 1][C - 1]
    ## 위
    for col in range(C - 1, 1, -1):
        board[bottom][col] = board[bottom][col - 1]
    board[bottom][1] = 0


for _ in range(T):
    spread_dust()
    clean_dust()


answer = 0
for r in range(R):
    for c in range(C):
        if board[r][c] > 0:
            answer += board[r][c]
print(answer)
