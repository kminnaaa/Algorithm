# 백준 1654

K, N = map(int, input().split())
array = []
for i in range(K):
    array.append(int(input()))

start = 1   # N의 min
end = max(array)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in array:
        count += i // mid
    if count >= N:  # 더 큰 수로 나눠야 하므로 start를 mid + 1로
        start = mid + 1
    else:   # 더 작은 수로 나눠야 하므로 end를 mid - 1로
        end = mid - 1
print(end)