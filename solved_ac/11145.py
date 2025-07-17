# Is it a Number?
# https://www.acmicpc.net/problem/11145

T = int(input())
for _ in range(T):
    line = input().strip()
    try:
        t = int(line)
        if " " in line or int(line) < 0:
            print("Invalid input")
        else:
            print(int(line))

    except:
        print("Invalid input")