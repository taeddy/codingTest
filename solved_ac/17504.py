N = int(input())

arr = list(map(int, input().split()))

P, Q = 1, arr[-1]

for idx in range(len(arr)-2, -1, -1):
    a = arr[idx]
    P, Q = Q, a*Q+P
P, Q = Q-P, Q
print(P, Q)

# 기약분수로 만들어야하는데 이대로 그냥 통과됨
# 원래는 P/Q를 약분해야함