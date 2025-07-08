# Ljeto
# https://www.acmicpc.net/problem/23401


def solution():
    n = int(input())
    score = {"pineapple": 0, "blueberry": 0}
    last_shot_time = {i: -11 for i in range(1, 9)}
    team_pineapple = [1, 2, 3, 4]
    team_blueberry = [5, 6, 7, 8]
    for _ in range(n):
        t, a, b = map(int, input().split())
        is_double_score = False

        if a in team_pineapple and b in team_blueberry:
            get_score = "pineapple"
        elif a in team_blueberry and b in team_pineapple:
            get_score = "blueberry"
        else:
            continue
        
        if t - last_shot_time[a] <= 10:
            is_double_score = True
        score[get_score] += 150 if is_double_score else 100
        last_shot_time[a] = t

    return score


print(*(solution().values()))
