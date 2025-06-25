# 암호 키
# https://www.acmicpc.net/problem/1816

N = int(input())

for _ in range(N):
    target = int(input())
    sig = True

    for n in range(2, 10**6):
        if target % n == 0:
            sig = False

    if sig:
        print("YES")
    else:
        print("NO")
