# 이진 검색 트리
# https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10**6)

order = []
while True:
    try:
        order.append(int(input()))
    except:
        break

# print(order)

def split_preorder(li):
    root = li.pop(0)
    idx = 0
    # 완전탐색
    for i in range(len(li)):
        if li[i] > root:
            idx = i
            break

    return root, li[:idx], li[idx:]
    
def pre_to_post(li):
    if len(li) == 1:
        return li
    elif len(li) == 0:
        return []
    root, left, right = split_preorder(li)
    return pre_to_post(left) + pre_to_post(right) + [root]

[print(i) for i in pre_to_post(order)]