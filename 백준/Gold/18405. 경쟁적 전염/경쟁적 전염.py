from collections import deque

N, K = map(int, input().split())

matrix = []
virus = []
for i in range(N):
  matrix.append(list(map(int, input().split())))
  for j in range(N):
    if matrix[i][j] != 0:
      virus.append((matrix[i][j], 0, i, j))

virus.sort()
q = deque(virus)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
  virus, s, x, y = q.popleft()
  if s == target_s:
    break

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < N:
      if matrix[nx][ny] == 0:
        matrix[nx][ny] = virus
        q.append((virus, s+1, nx, ny))

print(matrix[target_x - 1][target_y - 1])