# 시험장 나누기

class testCenter:
    left = None
    right = None
    num = -1
    persons = -1
    childsum = -1

    def __init__(self) -> None:
        pass

def calSubtree(center):
    if center.childsum != -1:
        return center.childsum
    center.childsum = center.persons
    for node in [center.left, center.right]:
        center.childsum += calSubtree(node) if node else 0
    return center.childsum

def cutSubtree(center, LR):
    # LR == 0: Left
    # LR == 1: Right
    target = center.right if LR else center.left
    center.childsum -= target.childsum
    if LR:
        center.right = None
    else:
        center.left = None
    return

def solution(k, num, links):
    answer = 0
    centers = [testCenter() for _ in num]
    for i, center in enumerate(centers):
        center.num = i
        center.persons = num[i]
        center.left = centers[links[i][0]] if links[i][0] != -1 else None
        center.right = centers[links[i][1]] if links[i][1] != -1 else None


    # 루트 찾기 -> 비효율적일듯
    # 루트 모르는 채로 진행
    for center in centers:
        calSubtree(center)
    
    t = [c.childsum for c in centers]
    # print(t)
    for _ in range(k-1):
        t = [c.childsum for c in centers]
        center = centers[t.index(max(t))]
        lc = center.left.childsum if center.left != None else None
        rc = center.right.childsum if center.right != None else None
        if lc == rc == None:
            break
        LR = 1 if lc == None else 0
        cutSubtree(center, LR)
    t = [c.childsum for c in centers]
    # print(t)
    answer = max(t)
    return answer

k = 3
num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]	
links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]	
solution(k, num, links)