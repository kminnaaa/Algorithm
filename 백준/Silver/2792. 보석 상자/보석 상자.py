# 백준 2792

import sys

N, M = map(int, sys.stdin.readline().split())
array = []
for _ in range(M):
    array.append(int(sys.stdin.readline()))

# mid = 질투심 일 때, N명에게 나누어줄 수 있는지

start = 1
end = max(array)
jealousy = 0

while start <= end:
    mid = (start + end) // 2
    total = 0   # 보석 받는 학생 수
    for j in array:
        if  (j % mid) == 0:
            total += (j // mid)
        else:
            total += ((j // mid) + 1)
    if total > N:
        start = mid + 1
    else:
        jealousy = mid
        end = mid - 1
print(jealousy)
