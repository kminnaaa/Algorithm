# 백준 2512

N = int(input())
array = list(map(int, input().split()))
M = int(input())

start = 0
end = max(array)
result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for i in array:
        total += min(i, mid)
    if total > M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)