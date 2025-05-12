# 백준 6236

N, M = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))

# N은 예산, M은 통장에서 뺄 수 있는 횟수
# 통장에서 K원 인출, 모자라면 남은 금액 통장에 넣고 다시 K원
# K 최소화

start = max(money)
end = sum(money)
mid = 0

while start <= end:
    mid = (start + end) // 2
    total = mid
    count = 1
    for i in money:
        if i > total:
            total = mid
            count += 1
        total -= i
    if count > M:
        start = mid + 1
    else:
        end = mid - 1
print(mid)