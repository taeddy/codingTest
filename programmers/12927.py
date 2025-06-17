# 야근 지수

import heapq

def solution(n, works):

    if n >= sum(works):
        return 0
    
    works = [-work for work in works]
    heapq.heapify(works)

    # print(works)

    for _ in range(n):
        target = heapq.heappop(works)
        target += 1
        heapq.heappush(works, target)
    
    # print(works)
    return sum([work**2 for work in works])






cases = [[[4, 3, 3], 4, 12], [[2, 1, 2], 1, 6], [[1,1], 3, 0]]
for case in cases:
    solution(case[1], case[0])