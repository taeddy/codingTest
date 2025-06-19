# 울타리 공사
# https://www.acmicpc.net/problem/32171

N = int(input())

# print(structure)
a, b, c, d = 10, 10, -10, -10
for i in range(N):
    new_a, new_b, new_c, new_d = map(int, input().split())
    # a, b 중에서 최소, c, d 중에서 최대 탐색
    a, b, c, d = min(a, new_a), min(b, new_b), max(c, new_c), max(d, new_d)
    w, h = c-a, d-b
    print(2*(w+h))