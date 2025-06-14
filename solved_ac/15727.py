L = int(input())

answer = L//5
answer += 1 if L % 5 != 0 else 0
print(answer)