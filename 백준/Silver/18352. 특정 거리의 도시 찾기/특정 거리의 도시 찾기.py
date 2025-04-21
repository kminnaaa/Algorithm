# 백준 18352

from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())  # 도시 개수, 간선 개수, 거리 정보, 출발 도시
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

def bfs(graph, x, distance):
    queue = deque([x])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[v] + 1
    answer = [i for i in range(1, n+1) if distance[i] == k]
    if answer:
        answer.sort()
        for i in answer:
            print(i)
    else:
        print(-1)
bfs(graph, x, distance)