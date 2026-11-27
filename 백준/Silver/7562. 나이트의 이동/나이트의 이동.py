from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        if x == dest_x and y == dest_y:
            return board[y][x]
        else:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < I and 0 <= ny < I and board[ny][nx] == 0:
                    board[ny][nx] = board[y][x] + 1
                    q.append((nx, ny))


T = int(input())

for _ in range(T):
    I = int(input())
    cur_x, cur_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())

    board = [[0] * I for _ in range(I)]

    ans = bfs(cur_x, cur_y)
    print(ans)