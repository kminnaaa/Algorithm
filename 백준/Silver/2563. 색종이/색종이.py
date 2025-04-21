# 백준 2563

N = int(input())
arr = [[0] * 100 for _ in range(100)]
answer = 0

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

for i in range(100):
    answer += arr[i].count(1)

print(answer)