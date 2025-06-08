N, D = map(int, input().split())

def flip(target, D):
    # D == 1 상하 반전
    # D == 2 좌우 반전
    _dict = {}
    _dict['d'] = ['q', 'b']
    _dict['b'] = ['p', 'd']
    _dict['q'] = ['d', 'p']
    _dict['p'] = ['b', 'q']
    return _dict[target][D-1]

for n in range(N):
    string = input()
    for s in string:
        print(flip(s, D),end='')
    print('')