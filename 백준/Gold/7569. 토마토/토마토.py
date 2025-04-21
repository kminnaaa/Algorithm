# 백준 7569 ? 헷갈림

from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())

dh = [0, 0, 0, 0, 1, -1]
dn = [0, 0, 1, -1, 0, 0]
dm = [-1, 1, 0, 0, 0, 0]

graph = []
for _ in range(h):
    arr = []
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    graph.append(arr)

queue = deque()
def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nh = z + dh[i]
            nn = x + dn[i]
            nm = y + dm[i]

            if 0 <= nh < h and 0 <= nn < n and 0 <= nm < m:
                if graph[nh][nn][nm] == 0:
                    graph[nh][nn][nm] = graph[z][x][y] + 1
                    queue.append((nh, nn, nm))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))
bfs()

day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit()
            day = max(day, graph[i][j][k])
print(day-1)