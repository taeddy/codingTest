s = set()
for _ in range(5):
    x = int(input())
    if x in s:
        s.remove(x)
    else:
        s.add(x)
print(*s)