# 3의 배수
# https://www.acmicpc.net/problem/1769

def cleaning(x: str):
    return str(sum(map(int, list(x))))

cnt = 0
X = input()
while len(X) > 1:
    X = cleaning(X)
    cnt += 1

print(cnt)
print('NO' if int(X) % 3 != 0 else 'YES')