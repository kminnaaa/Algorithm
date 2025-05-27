# 40 숨바꼭질

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
start = 1
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))     # a - b 비용 1
    graph[b].append((a, 1))     # b - a도 마찬가지

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 중복 확인
        if distance[now] < dist:
            continue
        
        # 현재노드와 연결된 모든 노드 체크
        for i in graph[now]:
            cost = dist + i[1]      # 거리 계산 (1씩 더해짐)

            # 더 짧은 경로 발견할 경우 갱신, push
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 제일 큰 비용 찾기
max_node = 0
max_distance = 0
result = []

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))