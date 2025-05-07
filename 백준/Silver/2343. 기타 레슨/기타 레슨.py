# 백준 2343

N, M = map(int, input().split())
array = list(map(int, input().split()))

# 블루레이의 크기를 기준으로 최소, 최대
start = max(array) 
end = sum(array)

while start <= end:
    mid = (start + end) // 2
    total = 0
    count = 1   # 블루레이 개수

    # 1. 앞에서부터 블루레이에 넣고,
    # 2. 넣다가, sum값이 mid(블루레이 길이)보다 커지면 블루레이 개수 + 1
    for time in array:
        if total + time > mid:
            count += 1
            total = 0
        total += time
    if count <= M:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)