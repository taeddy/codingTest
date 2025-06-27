# 암기왕
# https://www.acmicpc.net/problem/2776

T = int(input())

for _case in range(T):
    N = int(input())
    note_1 = set(map(int, input().split()))
    
    M = int(input())
    note_2 = list(map(int, input().split()))
    for num in note_2:
        if num in note_1:
            print(1)
        else:
            print(0)

