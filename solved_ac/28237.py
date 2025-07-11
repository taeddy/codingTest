# 수학 선생님의 고민(Easy)
# https://www.acmicpc.net/problem/28237

# (ax + b)(cx + d) = nx^2 + (n+1)x - (n+2)
# ac = n
# ad + bc = n+1
# bd = -(n+2)


def solution():
    n = int(input())
    for a in range(1, n + 1):
        if n % a == 0:
            c = n // a
            for b in range(-(n + 2), (n + 2) + 1):
                if b == 0 or -(n + 2) % b != 0:
                    continue
                d = -(n + 2) // b

                if a * d + b * c == n + 1:
                    return a, b, c, d
    return -1


res = solution()
if res == -1:
    print(res)
else:
    print(*res)
