# Selection of Participants of an Experiment
# https://www.acmicpc.net/problem/13280

while True:
    N = int(input())
    if N == 0:
        break
    a = list(map(int, input().split()))
    a.sort()
    b = []
    for i in range(len(a)-1):
        b.append(a[i+1]-a[i])
    print(min(b))