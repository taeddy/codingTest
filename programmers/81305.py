# 시험장 나누기
import sys
sys.setrecursionlimit(int(1e6))

def solution(k, num, links):
    answer = 0

    def find_root():
        has_parent = [False]*len(num)
        for l, r in links:
            if l != -1:
                has_parent[l] = True
            if r != -1:
                has_parent[r] = True
        return has_parent.index(False)
    
    def search(node, target):
        if node == -1:
            return 0, 0
        
        left, right = links[node]
        left_cnt, left_val = search(left, target)
        right_cnt, right_val = search(right, target)
        total_cnt = left_cnt+right_cnt
        
        if left_val + right_val + num[node] <= target:
            return total_cnt, left_val + right_val + num[node]
        elif min(left_val, right_val) + num[node] <= target:
            return total_cnt+1, min(left_val, right_val) + num[node]
        return total_cnt+2, num[node]
        
    def binary_search(start, end):
        result = end
        while start <= end:
            mid = (start+end)//2
            cnt, _ = search(root, mid)
            if cnt > k-1:
                start = mid+1
            else:
                result = min(result, mid)
                end = mid-1
        return result

    root = find_root()
    start, end = max(num), sum(num)
    answer = binary_search(start, end)
    return answer

# k = 3
# num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]	
# links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]	
# print(solution(k, num, links))