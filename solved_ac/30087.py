# 진흥원 세미나
# https://www.acmicpc.net/problem/30087

lectures = {
    'Algorithm': 204,
    'DataAnalysis': 207,
    'ArtificialIntelligence': 302,
    'CyberSecurity': 'B101',
    'Network': 303,
    'Startup': 501,
    'TestStrategy': 105
}

N = int(input())
for _ in range(N):
    line = input()
    print(lectures[line])