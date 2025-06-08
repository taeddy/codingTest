T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    count = 0
    for n in range(N, M+1):
        count += str(n).count('0')
    print(count)