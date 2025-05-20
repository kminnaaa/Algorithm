# 병사 배치하기 - 백준 18353

N = int(input())
arr = list(map(int, input().split()))
d = [1] * N

for i in range(N):
    for j in range(i):
        # 더 작은 경우에 값 할당
        if arr[i] < arr[j]:
            d[i] = max(d[i], d[j] + 1)

# 남아있는 병사의 수가 최대
print(N - max(d))