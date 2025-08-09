"""
flag 안 쓰고 마지막 처리 하려면 ????

1. exit() 즉시 프로그램 종료

2.
for-else
  : break 없이 정상 종료된 경우에 else 블록 실행
"""

from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 익은 토마토 위치 큐에 넣기
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내 o, 안 익은 토마토 발견 > 일수 +1
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))      # 다음 탐색 대상으로 저장

bfs()

res = 0
for row in tomato:
    # 아직 안 익은 거 있으면 -1
    if 0 in row:
        print(-1)
        exit()
    # 아닐 경우, max값으로 구해줌
    res = max(res, max(row))

print(res - 1)  # 익은 날이 1부터 시작하므로 -1 해야 실제 날짜