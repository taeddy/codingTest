# 이장님 초대
# https://www.acmicpc.net/problem/9237

N = int(input())

t = list(map(int, input().split()))

t.sort(key=lambda x: -x)

for i in range(1, len(t)+1):
    t[i-1] += i

print(max(t)+1)