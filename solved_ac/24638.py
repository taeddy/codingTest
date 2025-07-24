# Anno Domini 2022
# https://www.acmicpc.net/problem/24638

def to_int(line):
    if line[0] == 'AD':
        return int(line[1])
    else:
        return -int(line[0])

def sign(num):
    return (num > 0) - (num < 0)

line_1 = list(input().split())
line_2 = list(input().split())

x, y = to_int(line_1), to_int(line_2)

if sign(x) == sign(y):
    print(abs(x-y))
else:
    print(abs(x-y)-1)
