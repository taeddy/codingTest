# Polynomial Boundaries 
# https://www.acmicpc.net/problem/11327

while True:
    li = list(map(int, input().split()))
    if len(li) == 1:
        break

    a = li[1:]
    x, y = map(int, input().split())
    cal = 0
    co = 1
    for an in a:
        cal += co * an
        co *= x
    
    if cal > y:
        print('Inside')
    elif cal == y:
        print('On')
    else:
        print('Outside')