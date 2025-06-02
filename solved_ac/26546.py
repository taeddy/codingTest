cases = int(input())
for _ in range(cases):
    word, i, j = input().split()
    i, j = int(i), int(j)
    print(word[:i]+word[j:])