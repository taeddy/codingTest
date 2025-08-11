# Average is not Fast Enough!
# https://www.acmicpc.net/problem/6558

import math

arg = input().split()
n, d = int(arg[0]), float(arg[1])

while True:
    try:
        line = input()
    except:
        break

    line = line.split()
    t = int(line[0])

    total_sec = 0
    for idx in range(1, len(line)):
        record = line[idx]
        if '-' in record:
            total_sec = '-'
            break
        total_sec += int(record[0])*3600 + int(record[2:4])*60 + int(record[5:])

    if total_sec == '-':
        print(f'{t:3d}: -')
    else:
        speed = math.modf(total_sec/60/d)
        m, s = speed[1], round(speed[0]*60, 0)
        if s == 60:
            m += 1
            s = 0
        print(f'{t:3d}: {m:.0f}:{s:02.0f} min/km')
    
