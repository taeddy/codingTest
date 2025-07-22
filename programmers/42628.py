# 이중우선순위큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    li = []
    for operation in operations:
        op, num = operation.split()
        
        if op == 'I':
            li.append(int(num))
        elif op == 'D':
            if li:
                if num == '1':
                    li.pop(li.index(max(li)))
                elif num == '-1':
                    li.pop(li.index(min(li)))

    if li:
        return [max(li), min(li)]
    else:
        return [0, 0]
    

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))


