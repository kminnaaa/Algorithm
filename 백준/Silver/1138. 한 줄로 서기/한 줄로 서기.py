N = int(input())
line = list(map(int, input().split()))
ans = [0 for _ in range(N)]

count = 0
for i in range(N):
    for j in range(N):
        if count == line[i] and ans[j] == 0:
            ans[j] = i + 1
            break
        if ans[j] == 0: count += 1
    count = 0

print(*ans)