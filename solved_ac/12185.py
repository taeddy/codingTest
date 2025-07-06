# GBus count (Large)
# https://www.acmicpc.net/problem/12185


def solution():
    T = int(input())
    for testcase in range(T):
        N = int(input())
        buses = []
        line = list(map(int, input().split()))
        for idx in range(len(line) // 2):
            buses.append((line[2 * idx], line[2 * idx + 1]))

        can_serve_cnt = [0] * 5001
        for start, end in buses:
            for city in range(start, end + 1):
                can_serve_cnt[city] += 1

        P = int(input())
        want_to_know_cities = []
        for _ in range(P):
            want_to_know_cities.append(int(input()))
        result = []
        for city in want_to_know_cities:
            result.append(can_serve_cnt[city])

        print(f"Case #{testcase+1}:", end=" ")
        print(" ".join(map(str, result)))

        if testcase < T - 1:
            tmp = input()


solution()
