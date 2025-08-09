import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        if x == dest_x and y == dest_y:
            return graph[x][y]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

T = int(input())

for i in range(T):
    I = int(input())
    graph = [[0] * I for _ in range(I)]
    cur_x, cur_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())
    print(bfs(cur_x, cur_y))