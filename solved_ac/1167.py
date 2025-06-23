# 트리의 지름
# https://www.acmicpc.net/problem/1167

import heapq

V = int(input())
tree = {}

for _ in range(1, V+1):
    line = input().split()
    idx = int(line[0])
    li = []
    nodes = line[1:-1]
    for _ in range(len(nodes)//2):
        dest, cost = map(int, nodes[_*2:_*2+2])
        li.append((cost, dest))
    tree[idx] = li

def dijkstra(start):
    dist = {dest: float('inf') for dest in tree.keys()}
    queue = [(0, start)]
    dist[start] = 0

    while queue:
        cut_dist, cur_node = heapq.heappop(queue)
        for next_dist, next_node in tree[cur_node]:
            new_dist = cut_dist+next_dist
            old_dist = dist[next_node]
            if new_dist < old_dist:
                heapq.heappush(queue, (new_dist, next_node))
                dist[next_node] = new_dist

    return dist

distance = dijkstra(1)
max_node_idx = max(distance, key=distance.get)
distance = dijkstra(max_node_idx)
print(max(distance.values()))