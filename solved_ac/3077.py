# 임진왜란
# https://www.acmicpc.net/problem/3077

n = int(input())
correct = dict(zip(input().split(), [i for i in range(n)]))
submission = list(input().split())

import itertools

score = 0
li = list(itertools.combinations(submission, r=2))
for war1, war2 in li:
    if correct[war1] < correct[war2]:
        score += 1

print(f'{score}/{len(li)}')
