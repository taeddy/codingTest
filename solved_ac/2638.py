# 치즈
# https://www.acmicpc.net/problem/2638
from collections import deque

N, M = map(int, input().split())
board = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for _ in range(N):
    board.append(list(map(int, input().split())))

def check_around(r, c):
    pass

def make_outside():
    for col in range(M):
        board[0][col] = -1
        board[-1][col] = -1

    visited = []
    for _ in range(N):
        visited.append([0]*M)
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N and 0 <= ny < M) and visited[nx][ny] == 0 and board[nx][ny] != 1:
                board[nx][ny] = -1
                visited[nx][ny] = 1
                queue.append((nx, ny))

def check_all_melted():
    for row in board:
        cheese = row.count(1)
        if cheese:
            return False
    return True

def spread_outside(r, c):
    board[r][c] = -1
    queue = deque()
    queue.append((r, c))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = -1
                queue.append((nx, ny))

def will_melt():
    tmp = []
    for x in range(N):
        t = []
        for y in range(M):
            outside_count = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == -1:
                    outside_count += 1
            # if y == N-1:
            #     print(outside_count)
            # else:
            #     print(outside_count, end=' ')
            if outside_count >= 2:
                t.append(True)
            else:
                t.append(False)
        tmp.append(t)
    return tmp
    

def solution():
    time = 0
    while True:
        will_melt_board = will_melt()
        if check_all_melted():
            return time
        for row in range(N):
            for col in range(M):
                if will_melt_board[row][col]:
                    spread_outside(row, col)
        time += 1

make_outside()
ans = solution()
print(ans)


