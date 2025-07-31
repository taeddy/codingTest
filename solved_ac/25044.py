# 에어컨
# https://www.acmicpc.net/problem/25044

import sys
input = sys.stdin.readline

N, K = map(int, input().split())


# 에어컨 켜지는 시간
# 900 + x*(1440+K)
# 1080 + x*(1440+K)
# 1260 + x*(1440+K)

# N일의 period = N*1440 ~ (N+1)*1440
# period에 속하는 시간대 찾기.

# 1440+K >= 1440 이므로
x = N*1440//(1440+K)

def min2clock(mins):
    dd = (mins//60)//24
    hh = (mins//60)%24
    mm = mins%60
    return dd, f'{hh:02d}:{mm:02d}'

li = [900+x*(1440+K), 1080+x*(1440+K), 1260+x*(1440+K), 900+(x+1)*(1440+K), 1080+(x+1)*(1440+K), 1260+(x+1)*(1440+K)]

ans = []
for c in li:
    dd, t = min2clock(c)
    if dd == N:
        ans.append(t)

print(len(ans))
for a in ans:
    print(a)
