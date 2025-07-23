# 별 찍기 - 16
# https://www.acmicpc.net/problem/10991

def sol(height):
    if height == 1:
        return ['*']

    bf = sol(height-1)
    for idx in range(height-1):
        bf[idx] = ' '+bf[idx]
    bf.append(' '.join(['*']*height))

    return bf

ans = sol(int(input()))

[print(l) for l in ans]
