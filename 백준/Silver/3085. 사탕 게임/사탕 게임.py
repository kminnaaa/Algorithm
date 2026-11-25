N = int(input())
color = [list(input().strip()) for _ in range(N)]

def check():
    max_leng = 0
    for i in range(N):
        cnt = 1
        for j in range(N - 1):
            if color[i][j] == color[i][j + 1]:
                cnt += 1
            else:
                max_leng = max(cnt, max_leng)
                cnt = 1
        max_leng = max(cnt, max_leng)

    for i in range(N):
        cnt = 1
        for j in range(N - 1):
            if color[j][i] == color[j + 1][i]:
                cnt += 1
            else:
                max_leng = max(cnt, max_leng)
                cnt = 1
        max_leng = max(cnt, max_leng)

    return max_leng


ans = 1

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            if color[i][j] != color[i][j + 1]:
                color[i][j], color[i][j + 1] = color[i][j + 1], color[i][j]

                ans = max(ans, check())

                color[i][j], color[i][j + 1] = color[i][j + 1], color[i][j]

        if i + 1 < N:
            if color[i][j] != color[i + 1][j]:
                color[i][j], color[i + 1][j] = color[i + 1][j], color[i][j]

                ans = max(ans, check())

                color[i][j], color[i + 1][j] = color[i + 1][j], color[i][j]

print(ans)