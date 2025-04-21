# 백준 7562 bfs

from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        if x == destx and y == desty:
            return graph[x][y]

        for i in range(8):
            mx = x + dx[i]
            my = y + dy[i]

            if 0 <= mx < I and 0 <= my < I and graph[mx][my] == 0:
                graph[mx][my] = graph[x][y] + 1
                queue.append((mx, my))

n = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(n):
    I = int(input())
    graph = [[0]*I for i in range(I)]
    x, y = map(int, input().split())
    destx, desty = map(int, input().split())
    print(bfs(x, y))