board = [[0 for _ in range(100)] for _ in range(100)]

N = int(input())
ans = 0

for i in range(N):
    w, h = map(int, input().split())

    for j in range(10):
        for k in range(10):
            board[h + j][w + k] = 1

for sub in board:
    ans += sub.count(1)
print(ans)