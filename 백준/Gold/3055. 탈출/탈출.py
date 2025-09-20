"""
빈곳 . 물 * 돌 X
비버 굴 D 고슴도치 위치 S

고슴도치: 매분마다 인접한 네 칸 (상하좌우) 중 하나로 이동
물: 매분마다 비어있는 칸으로 확장 (상하좌우)
물, 고슴도치 > 돌 통과할 수 없음
고슴도치 > 물 통과 불가능, 물 > 비버 소굴 이동 x
고슴도치 > 비버 최소 시간
+ 물이 찰 예정인 칸으로 이동할 수 없다 (다음 시간에 물이 찰 예정인 칸)
"""

import sys
from collections import deque

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

visited = [[-1] * C for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque()


for i in range(R):
    for j in range(C):
        if board[i][j] == '*':
            q.append((i, j, 'w'))

for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            q.append((i, j, 'g'))
            visited[i][j] = 0

while q:
    x, y, t = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if t == 'w':
                if board[nx][ny] == '.':
                    board[nx][ny] = '*'
                    q.append((nx, ny, 'w'))
            else:
                if board[nx][ny] == 'D':
                    print(visited[x][y] + 1)
                    exit(0)

                if board[nx][ny] == '.' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny, 'g'))

print('KAKTUS')