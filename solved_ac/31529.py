# 2024년에는 혼자가 아니길
# https://www.acmicpc.net/problem/31529

# 재우 재현 재우s 재현s
# A    B    C    D

X, Y = map(int, input().split())

j = 2*X-Y
if j < 0 or X > Y:
    print(-1)
else:
    print(int(j/4*2024))
