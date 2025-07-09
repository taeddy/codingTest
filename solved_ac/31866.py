# 손가락 게임
# https://www.acmicpc.net/problem/31866

def solution():
    JS, IJ = map(int, input().split())
    if JS not in [0, 2, 5]: JS = 6
    if IJ not in [0, 2, 5]: IJ = 6
    
    if (JS, IJ) in [(0, 5), (5, 0)]:
        print('>') if JS > IJ else print('<')
    else:
        if JS > IJ:
            print('<')
        elif JS < IJ:
            print('>')
        else:
            print('=')

solution()