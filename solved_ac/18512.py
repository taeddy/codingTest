p1, p2, x, y = map(int, input().split())
LIMIT = 10**4 # 10**3까지 오답

xs = set(range(x, LIMIT, p1))
ys = set(range(y, LIMIT, p2))

ans = xs&ys

print(min(ans) if ans else -1)