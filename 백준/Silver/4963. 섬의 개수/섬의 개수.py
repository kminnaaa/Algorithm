import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]

def dfs(x, y):
    if 0 <= x < W and 0 <= y < H and board[y][x] == 1:
        if not visited[y][x]:
            visited[y][x] = True

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                dfs(nx, ny)


while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0: break

    board = [list(map(int, input().split())) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]

    ans = 0
    # 1 덩어리 세기...
    for y in range(H):
        for x in range(W):
            if board[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                ans +=1

    print(ans)    