# 파이프 옮기기 1
# https://www.acmicpc.net/problem/17070

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
# 각각 파이프 끝이 [세로, 가로, 대각선]인 경우의 수

for row in range(N):
    for col in range(1, N):
        # 기둥이 세워져 있는 경우
        if board[row][col] == 1:
            continue
        # 초기조건 (시작점)
        if row == 0 and col == 1:
            dp[row][col] = [0, 1, 0]
            continue

        # 위쪽 파이프(세로, 대각선)에서 오는 경우, 무조건 세로 모양으로 이어짐
        try:
            if board[row-1][col] == 0:
                dp[row][col][0] += dp[row-1][col][0] + dp[row-1][col][2]
        except:
            pass
        # 왼쪽 파이프(가로, 대각선)에서 오는 경우, 무조건 가로 모양으로 이어짐
        try:
            if board[row][col-1] == 0:
                dp[row][col][1] += dp[row][col-1][1] + dp[row][col-1][2]
        except:
            pass
        # 대각선에서 이어지는 경우(가로, 세로, 대각선), 대각선으로 이어짐
        try:
            if board[row-1][col-1] == board[row-1][col] == board[row][col-1] == 0:
                dp[row][col][2] += sum(dp[row-1][col-1])
        except:
            pass

# [print(d) for d in dp]
print(sum(dp[-1][-1]))