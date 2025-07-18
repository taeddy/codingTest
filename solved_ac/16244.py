# Spaceship 
# https://www.acmicpc.net/problem/16244

n = int(input())
f = list(map(int, input().split()))

target = sum(f)//2
idx_target = f.index(target)
print(*(f[:idx_target] + f[idx_target+1:]), target)
