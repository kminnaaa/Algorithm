from collections import deque

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(M)]

# 진우 위치: 0,0
# 거래소 위치: [M-1,N-1]
# 1이면 지나갈 수 있고, 0이면 지나갈 수 없음
# 오른쪽, 아래로만 이동 가능

dx = [1, 0]
dy = [0, 1]

def bfs():
    queue = deque([(0,0)])
    visited = [[False] * N for _ in range(M)]
    visited[0][0] = True
    
    while queue:
        y, x = queue.popleft()

        for i in range(2):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx] and city[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((ny, nx))

        if x == N - 1 and y == M - 1:
            return 'Yes'
    
    return 'No'

print(bfs())