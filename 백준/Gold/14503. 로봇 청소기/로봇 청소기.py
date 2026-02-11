import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

room = []
for i in range(N):
  row = list(map(int, input().split()))
  room.append(row)

answer = 0
while True:
  if room[r][c] == 0:
    room[r][c] = 2
    answer += 1
  
  flag = 0
  for i in range(4):
    d = (d - 1) % 4
    ny, nx = r + dy[d], c + dx[d]
    if 0 <= ny < N and 0 <= nx < M and room[ny][nx] == 0:
      r, c = ny, nx
      flag = 1
      break
  if flag:
    continue

  by, bx = r - dy[d], c - dx[d]
  if 0 <= by < N and 0 <= bx < M and room[by][bx] != 1:
    r, c = by, bx
  else:
    print(answer)
    break