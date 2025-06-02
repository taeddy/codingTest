# x, y가 유일하게 존재한다는 조건 하에 문제 풀이
# 따라서 아래의 y는 반드시 연산 가능함
# 그러나 x를 연산할 때에는 y를 이용하기 때문에, x의 계수가 0인 경우를 고려해야함

a, b, c, d, e, f = map(int, input().split())

y = (d*c-a*f)/(d*b-a*e)
x = (c-b*y)/a if a != 0 else (f-e*y)/d

print(int(x), int(y))