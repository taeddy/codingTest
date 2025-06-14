def PER():
    while True:
        yield from ['P', 'E', 'R']

code = input()
cnt = 0
for i, tmp in enumerate(PER()):
    if i >= len(code):
        break
    if code[i] != tmp:
        cnt += 1
print(cnt)