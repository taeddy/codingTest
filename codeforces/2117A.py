# False Alarm

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    # 0: opened
    # 1: closed

    first_closed_door_idx = a.index(1)
    can_pass_with_button_idx = first_closed_door_idx + x

    if can_pass_with_button_idx >= n:
        print('YES')
    else:
        if a[can_pass_with_button_idx:].count(1) == 0:
            print('YES')
        else:
            print('NO')