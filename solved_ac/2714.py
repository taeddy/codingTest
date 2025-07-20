# 문자를 받은 승환이
# https://www.acmicpc.net/problem/2714

T = int(input())
go = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(T):
    R, C, message = input().split()
    R, C = int(R), int(C)

    message = list(message)
    table = []
    for r in range(R):
        table.append(message[r * C : (r + 1) * C])
    visited = [[0]*C for _ in range(R)]

    flattened = []
    direction = 0
    x, y = 0, 0
    for i in range(R * C):
        flattened.append(table[x][y])
        visited[x][y] = 1

        nx, ny = x + go[direction][0], y + go[direction][1]
        if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0:
            x, y = nx, ny
        else:
            direction += 1
            if direction == 4:
                direction = 0
            x, y = x + go[direction][0], y + go[direction][1]
    flattened = ''.join(flattened)

    res = ''
    for i in range(len(flattened)//5):
        code = int(flattened[i*5:(i+1)*5], 2)
        if code != 0:
            s = chr(code+64)
        else:
            s = ' '
        res += s
    print(res.rstrip())
