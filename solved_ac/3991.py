# 한번 쏘면 멈출 수 없어
# https://www.acmicpc.net/problem/3991

h, w, c = map(int, input().split())
beads = list(map(int, input().split()))

next_bead = []
for i, bead in enumerate(beads):
    next_bead.extend([i+1]*bead)

ans = [[0]*w for _ in range(h)]

idx = 1
for i in range(w):
    for j in range(h):
        if not beads[idx-1]:
            idx += 1
        beads[idx-1] -= 1
        ans[j][i] = idx

[print(''.join(list(map(str, l)))) for l in ans]