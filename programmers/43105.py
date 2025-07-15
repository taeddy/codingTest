# 정수 삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105?language=python3

def solution(triangle):
    height = len(triangle)
    dp = []
    for _ in range(height):
        dp.append([0]*(_+1))

    for row in range(height-1):
        for col in range(row+1):
            new_value = dp[row][col] + triangle[row][col]
            dp[row+1][col] = max(dp[row+1][col], new_value)
            dp[row+1][col+1] = max(dp[row+1][col+1], new_value)

    for col in range(height):
        dp[-1][col] += triangle[-1][col]

    return max(dp[-1])
