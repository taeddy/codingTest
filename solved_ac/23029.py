# 시식 코너는 나의 것
# https://www.acmicpc.net/problem/23029

import sys
input = sys.stdin.readline
N = int(input())
foods = [int(input()) for _ in range(N)]

# dp로 하면 3가지 (현재 연속 시식횟수 = con 이라고 하면)
# con = 0 -> 먹거나(con=1) 말거나(con=0)
# con = 1 -> 먹거나(con=2) 말거나(con=0)
# con = 2 -> 안먹음(con=0)

# dp[i][0] = max(dp[i-1])
# dp[i][1] = dp[i-1][0] + foods[i]
# dp[i][2] = dp[i-1][1] + foods[i]

dp = [[0]*3 for _ in range(N)]
dp[0] = [0, foods[0], 0]
if N == 1:
    print(max(dp[0]))
else:
    dp[1] = [foods[0], foods[1], foods[0]+foods[1]//2]
    for i in range(2, N):
        dp[i][0] = max(dp[i-1])
        dp[i][1] = dp[i-1][0] + foods[i]
        dp[i][2] = dp[i-1][1] + foods[i]//2
    
    # [print(*l) for l in dp]
    print(max(dp[-1]))
