# 과자 나눠주기
# https://www.acmicpc.net/problem/16401

M, N = map(int, input().split())
L = list(map(int, input().split()))

start = 1
end = max(L)

ans = 0
while start <= end:
    mid = (start+end)//2

    cnt = 0
    for l in L:
        cnt += l // mid

    
    if cnt >= M: # 나누어 줄 수 있음 (길이 늘림)
        start = mid+1
        ans = mid
    else:
        end = mid-1

print(ans)
