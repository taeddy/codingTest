# 디지털 친구
# https://www.acmicpc.net/problem/1985

def are_friends(x, y):
    res = set(list(x)) ^ set(list(y))
    if res:
        return False
    else:
        return True

def are_almost_friends(x, y):
    x, y = list(x), list(y)
    for i in range(len(x)-1):
        if x[i] > '0' and x[i+1] < '9':
            x[i] = str(int(x[i])-1)
            x[i+1] = str(int(x[i+1])+1)
            if are_friends(x, y) and x[0] != '0':
                return True
            x[i] = str(int(x[i])+1)
            x[i+1] = str(int(x[i+1])-1)
        if x[i] < '9' and x[i+1] > '0':
            x[i] = str(int(x[i])+1)
            x[i+1] = str(int(x[i+1])-1)
            if are_friends(x, y) and x[0] != '0':
                return True
            x[i] = str(int(x[i])-1)
            x[i+1] = str(int(x[i+1])+1)
    return False

for _ in range(3):
    x, y = input().split()
    if are_friends(x, y):
        print('friends')
    elif are_almost_friends(x, y):
        print('almost friends')
    elif are_almost_friends(y, x):
        print('almost friends')
    else:
        print('nothing')
        
        
