# 백준 2805

import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(array)
result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            total += i - mid
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)