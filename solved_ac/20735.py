# Fifty Shades of Pink
# https://www.acmicpc.net/problem/20735

def solution():
    N = int(input())
    count = 0
    for _ in range(N):
        color_name = input()
        color_name = color_name.lower()
        if "rose" in color_name or "pink" in color_name:
            count += 1
    if count:
        print(count)
    else:
        print("I must watch Star Wars with my daughter")


solution()