T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    matrix = [[0] * N for _ in range(N)]

    # 우 하 좌 상
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    x, y = 0, 0
    i = 0

    for num in range(1, N**2 + 1):
        matrix[y][x] = num

        ny = y + dy[i]
        nx = x + dx[i]

        if not (0 <= ny < N and 0 <= nx < N) or matrix[ny][nx] != 0:
            i = (i + 1) % 4
            ny = y + dy[i]
            nx = x + dx[i]
        
        y, x = ny, nx


    print(f"#{tc}")
    for row in matrix:
        print(*row)