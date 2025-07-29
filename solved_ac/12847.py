# 꿀 아르바이트
# https://www.acmicpc.net/problem/12847

n, m = map(int, input().split())
t = list(map(int, input().split()))

dp = [0]*n
ans = sum(t[0:m])
new = ans

for idx in range(m, n):
    new = new - t[idx-m] + t[idx]
    ans = max(ans, new)

print(ans)
