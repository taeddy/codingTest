p = [float(input()) for _ in range(10)]
p.sort()
# print(p)

answer = 1
for i in range(1, 10):
    answer *= p[i]/i*10

print(f'{answer:.6f}')