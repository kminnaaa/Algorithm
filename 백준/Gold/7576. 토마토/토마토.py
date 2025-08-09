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
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))

bfs()

res = 0
for row in tomato:
    if 0 in row:
        print(-1)
        break
    res = max(res, max(row))
else:
    print(res - 1)  # 익은 날이 1부터 시작하므로 -1 해야 실제 날짜
