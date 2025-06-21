# 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

import heapq

def can_transform_old_ver(w1, w2):
    for idx in range(len(w1)):
        if w1[idx] != w2[idx] and w1[:idx] == w2[:idx] and w1[idx+1:] == w2[idx+1:]:
            return True
    return False

def can_transform(w1, w2):
    cnt = 0
    for c1, c2 in zip(w1, w2):
        if c1 == c2:
            cnt += 1
    if cnt == len(w1)-1:
        return True
    else:
        return False

def solution(begin: str, target: str, words: list) -> int:
    if target not in words:
        return 0
    
    dist = {word: 99 for word in words}
    
    def dijkstra():
        cnt = [99]*len(words)
        queue = [(0, begin)]

        while queue:
            # print(dist)
            now_cnt, now_word= heapq.heappop(queue)
            for new_word in words:
                if can_transform(now_word, new_word):
                    old_cnt = dist[new_word]
                    new_cnt = now_cnt + 1
                    if new_cnt < old_cnt:
                        dist[new_word] = new_cnt
                        heapq.heappush(queue, (new_cnt, new_word))
        return cnt

    dijkstra()
    answer = dist[target]
    if answer == 99:
        return 0
    else:
        return answer


# print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))