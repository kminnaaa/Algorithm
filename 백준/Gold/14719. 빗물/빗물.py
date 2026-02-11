# 14719

# 블록 높이: 0~H, 블록 개수: W개
H, W = map(int, input().split())
heights = list(map(int, input().split()))

# 빗물이 고이는 조건
# 왼쪽, 오른쪽에 벽 있어야 하고
# 두 벽 사이에 두 벽보다 낮은 구간이 있어야 함
# 
# 그 이전 구간은 물 채움
# 구간별로 기록하고 갱신하는 과정

# 현재칸 기준 좌우에 더 큰 칸 (벽) 있고, 현재칸이 둘중 작은칸보다 작으면 고일 수 있음

ans = 0
for i in range(1, W - 1):
    left = max(heights[:i])
    right = max(heights[i+1:])
    target = min(left, right)

    if heights[i] < target:
        ans += (target - heights[i])

print(ans)