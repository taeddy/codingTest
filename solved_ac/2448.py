# 별 찍기 - 11
# https://www.acmicpc.net/problem/2448
import math

N = int(input())
k = int(round(math.log(N / 3, 2), 0))

stars = ["  *  ", " * * ", "*****"]

def enlarge(old_stars):
    new_stars = []
    left_blank = len(old_stars[-1])//2+1
    
    # up side
    for star in old_stars:
        new_stars.append(" "*left_blank+star+" "*left_blank)
        
    # left side
    new_stars.extend(old_stars)
    
    # right side
    for old_idx, new_idx in enumerate(range(len(old_stars), len(old_stars)*2)):
        # print(old_stars[old_idx])
        new_stars[new_idx] += " " + old_stars[old_idx]
        
    return new_stars

for _ in range(k):
    stars = enlarge(stars)

[print(star) for star in stars]