# 선택 가능성이 가장 높은 자료형
# https://www.acmicpc.net/problem/32278

N = int(input())

if -(2**15) <= N <= 2**15-1:
    print('short')
elif -(2**31) <= N <= 2**31-1:
    print('int')
else:
    print('long long')