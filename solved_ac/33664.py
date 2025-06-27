# 현실적인 생일 축하 방안
# https://www.acmicpc.net/problem/33664

B, N, M = map(int, input().split())

item_list = {}
for _ in range(N):
    k, v = input().split()
    item_list[k] = int(v)

acc = 0
for _ in range(M):
    item_name = input()
    acc += item_list[item_name]

if acc <= B:
    print('acceptable')
else:
    print('unacceptable')