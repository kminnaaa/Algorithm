# 백준 3020

import bisect
import sys

arr1 = []   # 석순
arr2 = []   # 종유석
N, H = map(int, sys.stdin.readline().split())
for i in range(N):
    if i % 2 == 0:
        arr1.append(int(sys.stdin.readline()))
    else:
        arr2.append(int(sys.stdin.readline()))
arr1.sort()
arr2.sort()

# 높이 1 ~ h까지 구간 h개
# 1구간 지날 때 만나는 장애물: arr1에서 값이 1 이상, arr2에서 값이 h-1+1 이상
# 2구간 : arr2에서 값이 2 이상, arr2에서 값이 h-2+1 이상
# ...
count = []
for h in range(1, H+1):
    count.append((len(arr1) - bisect.bisect_left(arr1, h)) + (len(arr2) - bisect.bisect_left(arr2, H-h+1)))
print(min(count), count.count(min(count)))