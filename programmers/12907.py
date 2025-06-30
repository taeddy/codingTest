# 거스름돈
# https://school.programmers.co.kr/learn/courses/30/lessons/12907
import sys

sys.setrecursionlimit(10**9)

DEBUGPRINT = False


# 재귀
def recursion(n, money, acc):
    if not money:
        return 0
    cur_money = money[0]

    res = 0
    last = None
    for cur_used in range(n // cur_money + 1):
        remain = n - cur_used * cur_money
        if remain == 0:
            if DEBUGPRINT:
                print(
                    f"total: {n}, used coins: {acc}, cur money: {cur_money, cur_used}"
                )
            res += 1
            break

        res += recursion(remain, money[1:], acc + [(cur_money, cur_used)])

    return res


# dp
def dynamic_programming(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    for m in money:
        for charge in range(1, n + 1, 1):
            if charge - m >= 0:
                dp[charge] += dp[charge - m]
    return dp[-1]


def solution(n, money):

    money.sort(key=lambda x: -x)

    # return recursion(n, money, []) % 1000000007
    return dynamic_programming(n, money) % 1000000007


print(solution(5, [1, 2, 5]))  # 4
