# FA수의 진
# https://www.acmicpc.net/problem/31883


# 몇 초 지나야 초록불이 되는지 계산
def when_turn_green(C, D, cur_time):
    cur_time %= C + D
    if cur_time < C:
        return 0
    else:
        return C + D - cur_time


def solution():
    N = int(input())

    cur_time = 0
    for _ in range(N):
        A, B, C, D = map(int, input().split())
        time_footbridge = cur_time + B
        time_cross = cur_time + when_turn_green(C, D, cur_time=cur_time) + A

        if time_footbridge < time_cross:
            cur_time = time_footbridge
        else:
            cur_time = time_cross

    print(cur_time)


solution()
