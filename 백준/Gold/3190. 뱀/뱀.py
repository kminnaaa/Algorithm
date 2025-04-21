# 백준 3190

N = int(input())
K = int(input())
board = [[0] * (N + 1) for _ in range(N + 1)] # 1~N 사용
dir = []

for _ in range(K):
    a, b = map(int, input().split())
    board[a][b] = 1
L = int(input())
for _ in range(L):
    X, C = input().split()
    dir.append((int(X), C))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, C):
    if C == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    board[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx <= N and 1 <= ny <= N and board[nx][ny] != 2:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < L and time == dir[index][0]:
            direction = turn(direction, dir[index][1])
            index += 1
    return time
print(simulate())