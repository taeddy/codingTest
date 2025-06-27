# Σ
# https://www.acmicpc.net/problem/13172
MOD = 1000000007


def power_advanced(number, exp):
    if exp == 1:
        return number

    if exp % 2 == 0:
        half = power_advanced(number, exp // 2)
        return half * half % MOD
    else:
        return power_advanced(number, exp - 1) * number % MOD


def get_expected_value(numerator, denominator):
    return (numerator * power_advanced(denominator, MOD - 2)) % MOD


M = int(input())
answer = 0
for _ in range(M):
    v1, v2 = map(int, input().split())
    answer += get_expected_value(v2, v1)
print(answer % MOD)
