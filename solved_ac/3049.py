# 다각형의 대각선  
# https://www.acmicpc.net/problem/3049

import sys
input = sys.stdin.readline

N = int(input())
ans = N*(N-1)*(N-2)*(N-3)/24
print(int(ans))
