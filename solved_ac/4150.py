# 피보나치 수
# https://www.acmicpc.net/problem/4150

N = int(input())

fibonacci = [1, 1]

if N < 3:
    print(fibonacci[N - 1])
else:
    for _ in range(N - 2):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(fibonacci[-1])
