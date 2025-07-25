# 너의 평점은
# https://www.acmicpc.net/problem/25206

trans = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

grade_sum = 0
gp_sum = 0

for _ in range(20):
    lecture_name, grade, level = input().split()
    if level == 'P':
        continue
    grade_sum += float(grade)
    gp_sum += float(grade)*trans[level]

print(gp_sum/grade_sum)
