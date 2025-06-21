# 사이클 단어
# https://www.acmicpc.net/problem/1544

N = int(input())

words = []
for _ in range(N):
    # print(words)
    target = input()
    _target_in_words = False
    for word in words:
        if len(target) != len(word)//2:
            continue
        if target in word:
            _target_in_words = True
            break
    if not _target_in_words:
        words.append(target+target)
print(len(words))