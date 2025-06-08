cases = int(input())

ans = [0, 0, 0, 0]

for case in range(cases):
    g, c, n = map(int, input().split())
    if g == 1:
        ans[3] += 1
    elif c <= 2:
        ans[0] += 1
    elif c == 3:
        ans[1] += 1
    elif c == 4:
        ans[2] += 1

for a in ans:
    print(a)