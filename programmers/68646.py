# 풍선 터트리기
# https://school.programmers.co.kr/learn/courses/30/lessons/68646

'''
최후까지 남으려면 특정 요소 a[i]를 기준으로 a[:i]와 a[i+1:]를 살펴보았을 때
a[i]보다 큰것만 있으면 남겨놓을 수 있다. (작은게 생존)

근데 작은 풍선을 고를 기회가 1번 있으니까
1. a[:i]에 a[i]보다 작은 풍선 있음
2. a[i+1:]에 a[i]보다 작은 풍선 있음
위 1, 2의 경우에도 가능해진다.

그럼 특정 요소 a[i]를 남기지 못하는 경우는 그 반대로
a[:i]와 a[i+1:]에 각각 a[i]보다 작은 요소가 있으면 된다.

한줄요약: a[i] 보다 작은 풍선 양쪽에 있으면 남기기 불가능
'''

def solution(a):
    # a[i]보다 작은값이 있으면 True
    dp = [[0]*len(a) for _ in range(2)]

    min_left, min_right = float('inf'), float('inf')
    for idx in range(len(a)):
        cur_left = a[idx]
        cur_right = a[-idx-1]
        
        if min_left < cur_left:
            dp[0][idx] = 1
        elif min_left > cur_left:
            min_left = cur_left
            
        if min_right < cur_right:
            dp[1][-idx-1] = 1
        elif min_right > cur_right:
            min_right = cur_right
    
    cnt = 0
    for idx in range(len(a)):
        if dp[0][idx] + dp[1][idx] != 2:
            cnt += 1

    return cnt
