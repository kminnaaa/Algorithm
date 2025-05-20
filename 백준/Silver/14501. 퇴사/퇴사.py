# 퇴사 - 백준 14501

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
d = [0] * (N+1)

for i in range(N):
    for j in range(i + arr[i][0], N+1):
        if d[j] < d[i] + arr[i][1]:
            d[j] = d[i] + arr[i][1]
print(d[-1])