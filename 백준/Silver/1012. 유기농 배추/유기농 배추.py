import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M:
            if not visited[ny][nx] and ground[ny][nx] == 1:

                dfs(ny, nx)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    location = [list(map(int, input().split())) for _ in range(K)]
    ground = [[0] * M for _ in range(N)]

    visited = [[False] * M for _ in range(N)]

    for i in range(K):
        x, y = location[i]
        ground[y][x] = 1
    
    ans = 0

    # 배추 덩어리 개수를 세어야 함.... dfs?
    for y in range(N):
        for x in range(M):
            # 1. 방문 여부 검사 & 1인지 2. dfs 호출
            if ground[y][x] == 1 and visited[y][x] == False:
                dfs(y, x)
                ans += 1

    print(ans)