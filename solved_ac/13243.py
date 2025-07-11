# Non-decreasing subsegment
# https://www.acmicpc.net/problem/13243


def solution():
    n = int(input())
    numbers = list(map(int, input().split()))
    dp = [(1, numbers[0])]

    for idx in range(1, n):
        if numbers[idx] >= numbers[idx - 1]:
            new_length = dp[idx - 1][0] + 1
            new_sum = dp[idx - 1][1] + numbers[idx]
        else:
            new_length = 1
            new_sum = numbers[idx]
        dp.append((new_length, new_sum))
    
    res_idx = dp.index(max(dp, key=lambda x: x[0]))

    print(*dp[res_idx])


solution()
