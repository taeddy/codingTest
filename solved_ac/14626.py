ISBN = input()

weight = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
total = 0
error_weight = 0
for i, x in enumerate(ISBN):
    if i == 12:
        total += int(x)
    else:
        if x != '*':
            total += weight[i] * int(x)
        else:
            error_weight = weight[i]

for k in range(10):
    new = total + k * error_weight
    if new % 10 == 0:
        print(k)
        break