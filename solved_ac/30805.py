# 사전 순 최대 공통 부분 수열
# https://www.acmicpc.net/problem/30805

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

def solution(arr1, arr2, ans):
    if (not arr1) or (not arr2):
        return ans
    max1, max2 = max(arr1), max(arr2)
    idx1, idx2 = arr1.index(max1), arr2.index(max2)

    if max1 == max2:
        ans.append(max1)
        return solution(arr1[idx1+1:], arr2[idx2+1:], ans)
    elif max1 > max2:
        arr1.pop(idx1)
        return solution(arr1, arr2, ans)
    else:
        arr2.pop(idx2)
        return solution(arr1, arr2, ans)

ans = solution(A, B, [])

print(len(ans))
if ans:
    print(*ans)
    
