# 혼자 하는 윷놀이
# https://www.acmicpc.net/problem/24467

import sys

def solution():
    input = sys.stdin.readline

    # course: which path we're on (0: outer loop, 1: first diagonal, 2: fastest, 3: other diagonal)
    course = 0
    # idx: steps taken along the current course
    idx = 0
    is_win = False

    # Simulate up to 10 turns (extra throws don't count as a turn)
    for _ in range(10):
        line = input().rstrip()
        if not line:
            break
        # Count number of front faces (1s). 0 means all backs, 4 means all fronts.
        ones = sum(map(int, line))
        # Handle extra throws: all backs (0->move 4), all fronts (4->move 5)
        while ones == 0 or ones == 4:
            if ones == 0:
                idx += 4  # 윷 (all backs)
            else:
                idx += 5  # 모 (all fronts)
            line = input().rstrip()
            ones = sum(map(int, line))

        # Regular throws: move according to number of backs (4 - ones)
        if ones == 3:
            idx += 1  # 도
        elif ones == 2:
            idx += 2  # 개
        elif ones == 1:
            idx += 3  # 걸

        # Update course and check for branch points or finish
        if course == 0:
            if idx == 5:
                # First branch (to route 1)
                course = 1
                idx = 0
            elif idx == 10:
                # Second branch (to route 3)
                course = 3
                idx = 0
            elif idx >= 21:
                # Finished outer loop + 1
                is_win = True
        elif course == 1:
            if idx == 3:
                # Branch to fastest route
                course = 2
                idx = 0
            elif idx >= 12:
                # Finished route 1 + 1
                is_win = True
        elif course == 2:
            if idx >= 4:
                # Finished fastest route + 1
                is_win = True
        elif course == 3:
            if idx >= 7:
                # Finished other diagonal route + 1
                is_win = True

    # Output result
    print("WIN" if is_win else "LOSE")

if __name__ == '__main__':
    solution()
