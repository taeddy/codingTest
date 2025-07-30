# Triangles 
# https://www.acmicpc.net/problem/7595

import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        print('*'*(i+1))
