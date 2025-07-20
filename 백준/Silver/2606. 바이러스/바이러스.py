"""
a <> b 양방향 연결
"""
def dfs(v):
  visited[v] = 1
  for i in graph[v]:
    if visited[i] == 0:
      dfs(i)

N = int(input())
M = int(input())

visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
  a, b = list(map(int, input().split()))
  graph[a].append(b)
  graph[b].append(a)

dfs(1)
print(sum(visited) - 1)