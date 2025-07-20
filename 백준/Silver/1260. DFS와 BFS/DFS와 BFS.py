"""
정점 번호 작은 것부터 방문, 양방향 그래프
"""

from collections import deque

def dfs(start):
  visited_d[start] = True
  print(start, end=" ")

  for i in graph[start]:
    if not visited_d[i]:
      dfs(i)

def bfs(start):
  queue = deque([start])
  visited_b[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=" ")
    for i in graph[v]:
      if not visited_b[i]:
        visited_b[i] = True
        queue.append(i)

N, M, V = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  graph[a].sort()
  graph[b].sort()

visited_d = [False] * (N+1)
visited_b = [False] * (N+1)
dfs(V)
print()
bfs(V)