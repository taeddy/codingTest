# 노래 악보
# https://www.acmicpc.net/problem/1392

N, Q = map(int, input().split())

notes = [int(input()) for _ in range(N)]
questions = [int(input()) for _ in range(Q)]

acc_notes = [notes[0]]
for idx in range(1, len(notes)):
    acc_notes.append(acc_notes[idx-1] + notes[idx])

# print(notes)
# print(acc_notes)

for question in questions:
    for i, acc in enumerate(acc_notes):
        if question < acc:
            print(i+1)
            break