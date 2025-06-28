# 서강그라운드
# https://www.acmicpc.net/problem/14938
INF = int(1e9)

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

# 거리 초기화
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

# 간선 입력
for _ in range(r):
    a, b, l = map(int, input().split())
    dist[a - 1][b - 1] = l
    dist[b - 1][a - 1] = l

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 각 시작 지점에서 아이템 수 합산
max_item = 0
for i in range(n):
    total = 0
    for j in range(n):
        if dist[i][j] <= m:
            total += items[j]
    max_item = max(max_item, total)

print(max_item)
