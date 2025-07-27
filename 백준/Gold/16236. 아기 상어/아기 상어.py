"""
BFS?

자기보다 작은 물고기 먹을 수 있고, 크기 같은 물고기는 지나가는 것만 가능

거리 가까운 물고기가 많다면 가장 위에 있는 것
그런 게 여러 마리라면 가장 왼쪽에 있는 것

먹을 때마다 시간 증가
상어 크기만큼 물고기 먹으면 상어 크기 + 1
"""

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

# 상, 좌, 우, 하 순서
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 상어 크기, 걸린 시간, 먹은 물고기 개수
shark_size = 2
time = 0
fish_count = 0

# 상어 초기 위치 (9 찾기)
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark_x, shark_y = i, j     # 위치 저장하고
            board[i][j] = 0     # 초기화

def bfs(x, y, size):
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((x, y, 0))     # x, y, 이동 거리
    visited[x][y] = True
    fish_list = []      # 먹을 수 있는 물고기들

    while q:
        # 현재 위치
        cur_x, cur_y, dist = q.popleft()

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 지나갈 수 있는 칸 (작거나 같은 물고기)
                if board[nx][ny] <= size:
                    visited[nx][ny] = True
                    # 먹을 수 있는 물고기 (작은 물고기)
                    if 0 < board[nx][ny] < size:
                        fish_list.append((dist + 1, nx, ny))
                    q.append((nx, ny, dist + 1))
    return sorted(fish_list)    # 거리순, 거리 같으면 x(더 작은 = 위), 그 다음 y(더 작은 = 왼)

while True:
    fishes = bfs(shark_x, shark_y, shark_size)

    # 더 먹을 수 있는 물고기 없으면 종료
    if not fishes:
        break

    # 정렬된 상태이므로 앞에서부터 선택
    dist, fish_x, fish_y = fishes[0]

    # 상어 물고기 위치로 이동
    shark_x, shark_y = fish_x, fish_y
    board[fish_x][fish_y] = 0   # 먹고 초기화
    fish_count += 1
    time += dist    # 이동 거리만큼 시간 증가

    if fish_count == shark_size:
        shark_size += 1
        fish_count = 0

print(time)