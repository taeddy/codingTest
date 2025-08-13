# 팰린드로미터
# https://www.acmicpc.net/problem/4096

def str_plus_one(s):
    l = len(s)
    if s.count('9') == l:
        return '1'+'0'*len(s)
    else:
        return f'{int(s)+1:0{l}d}'

def is_palindrome(s):
    sig = True
    for s1, s2 in zip(s, reversed(s)):
        if s1 != s2:
            sig = False
            break
    return sig

while True:
    n = input()
    if n == '0':
        break

    cnt = 0
    while True:
        if is_palindrome(n):
            break
        cnt += 1
        n = str_plus_one(n)
    print(cnt)
    
