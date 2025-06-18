# Larger Sport Facility
# https://www.acmicpc.net/problem/16099

cases = int(input())

for _ in range(cases):
    lt, wt, le, we = map(int, input().split())

    tele = sorted([lt, wt])
    euro = sorted([le, we])

    if tele[0] < euro[0] and tele[1] < euro[1]:
        print('Eurecom')
    elif tele[0] > euro[0] and tele[1] > euro[1]:
        print('TelecomParisTech')
    else:
        dt = lt*wt
        de = le*we
        if dt > de:
            print('TelecomParisTech')
        elif dt < de:
            print('Eurecom')
        else:
            print('Tie')
