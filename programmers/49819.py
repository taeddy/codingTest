# 가장 먼 노드
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # 큐 형식: (거리, 노드)
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        if distances[cur_node] < cur_dist:
            distances[cur_node] = cur_dist
            continue
        for dest in graph[cur_node]:
            new_dist = cur_dist + 1
            if new_dist < distances[dest]:
                distances[dest] = new_dist
                heapq.heappush(queue, [new_dist, dest])
    
    return distances

def solution(n, edge):
    # n: 노드의 개수
    # edge: 간선 정보

    # dijkstra 활용

    answer = 0

    graph = {}
    for v1, v2 in edge:
        if graph.get(v1):
            graph[v1].append(v2)
        else:
            graph[v1] = [v2]
        if graph.get(v2):
            graph[v2].append(v1)
        else:
            graph[v2] = [v1]
    # print(graph)

    distances = list(dijkstra(graph, 1).values())
    
    return distances.count(max(distances))

# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
