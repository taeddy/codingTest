# 세로 읽기
# https://www.acmicpc.net/problem/10798

words = []
max_len = 0
for _ in range(5):
    s = input()
    max_len = max(max_len, len(s))
    words.append(s)

# print(words, max_len)
for idx in range(max_len):
    for word in words:
        try:
            print(word[idx], end='')
        except:
            pass