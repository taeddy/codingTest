# -2진수
# https://www.acmicpc.net/problem/2089

import sys
input = sys.stdin.readline

# 2진수 하듯이 -2진수 해보자

N = int(input())
if N == 0:
    print(0)
else:
    ans = []
    while N != 0:
        if N % (-2) != 0:
            ans.append('1')
            N = N//-2+1 # 음수 나눗셈의 몫은 소수가 trunc되므로 +1 해줘야한다.
        else:
            ans.append('0')
            N = N//-2
    
    print(''.join(ans[::-1]))
