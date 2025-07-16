# 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162
from collections import deque

def spread(computer_no, computers, computers_label):
    queue = deque([computer_no])
    while queue:
        cur_com = queue.popleft()
        for next_com in range(len(computers[0])):
            if computers_label[next_com] == 0 and computers[cur_com][next_com] == 1:
                computers_label[next_com] = computers_label[cur_com]
                queue.append(next_com)
    return computers_label
    

def solution(n, computers):
    
    computers_label = [0]*n
    now_com = 0
    while True:
        if computers_label.count(0) == 0:
            break
        else:
            now_com = computers_label.index(0)
        now_com = computers_label.index(0)
        computers_label[now_com] = max(computers_label)+1
        computers_label = spread(now_com, computers, computers_label)
    
    answer = max(computers_label)
    return answer
