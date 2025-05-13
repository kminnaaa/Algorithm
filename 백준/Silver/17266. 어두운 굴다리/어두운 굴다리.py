# 백준 17266

N = int(input())
M = int(input())
x = sorted(list(map(int, input().split())))

start = 1
end = N
result = 0

while start <= end:
    mid = (start + end) // 2    # 가로등 높이
    flag = 1
    if x[0] - mid > 0:
        flag = 0
    if x[-1] + mid < N:
        flag = 0
    for i in range(1, M):
        if x[i] - mid > x[i - 1] + mid:
            flag = 0
            break
    if flag:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)