M, N, K = map(int, input().split())
for m in range(M):
    line = input()
    for _ in range(K):
        for s in line:
            for _ in range(K):
                print(s, end='')
        print('')
    