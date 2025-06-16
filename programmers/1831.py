# 4단 고음
import math

def getRemainMul(n):
    return int(math.log(n)/math.log(3))

def getSimulation(n, numMul, numPlus):
    if numMul*2 < numPlus:
        return 0
    if n == 3 and numMul == 1 and numPlus == 0:
        return 1
    if n == 4 and numMul == 1 and numPlus == 1:
        return 1
    if n == 5 and numMul == 1 and numPlus == 2:
        return 1
    
    cnt = 0
    for i in range(numPlus+1):
        if n-i > 0 and (n-i)%3 == 0:
            cnt += getSimulation((n-i)/3, numMul-1, numPlus-i)
    return cnt

def solution(n):
    numMul = getRemainMul(n)
    numPlus = numMul * 2
    answer = getSimulation(n-2, numMul, numPlus-2)
    return answer

testcases = [[15, 1], [24, 0], [41, 2], [2147483647, 1735]]
for case in testcases:
    print(solution(case[0]), 'answer = ', case[1])
# solution(15)