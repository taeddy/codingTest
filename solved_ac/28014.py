N = int(input())
H = list(map(int, input().split()))
cnt = 0
last = -1
for h in H:
    if h >= last:
        cnt += 1
    last = h
print(cnt)