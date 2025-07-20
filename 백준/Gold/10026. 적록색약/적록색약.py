"""
같은 색 = 같은 구역
같은 색상 상하좌우 인접해있는 경우, 두 글자는 같은 구역

색약일 경우에는 R이랑 G 그냥 같은 문자로 ...

visited 별도로 만들면 bfs에서 처리할 때 에러
출력 처리 ?? end = ' '

색약일 때 4로 에러남 > R로 바꿔줄때 등호 실수 .. 
"""
from collections import deque

def bfs(x, y):
  q = deque()
  q.append([x, y])
  visited[x][y] = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < N) and (0 <= ny < N):
        if grid[nx][ny] == grid[x][y] and visited[nx][ny] == 0:
          q.append([nx, ny])
          visited[nx][ny] = 1

N = int(input())

grid = [list(input()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 색약 x
count = 0
for i in range(N):
  for j in range(N):
    if visited[i][j] == 0:
      bfs(i, j)
      count += 1
print(count, end=' ')

# 색약
for i in range(N):
  for j in range(N):
    if grid[i][j] == 'G':
      grid[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
count = 0
for i in range(N):
  for j in range(N):
    if visited[i][j] == 0:
      bfs(i, j)
      count += 1

print(count)