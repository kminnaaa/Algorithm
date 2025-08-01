"""
NxN 에서,
일정 높이 이하 모든 지점이 물에 잠김
  > 물에 잠기지 않는 영역
  = 물에 잠기지 않는 지점이 상하좌우로 인접해있고
     그 크기가 최대인 영역 (꼭짓점만 닿은 건 x)
  안전 영역의 최대 개수를 계산

  마지막에 for문 어떻게 돌지 ... maxheight 까지 > NxN?
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

min_h = 1000
max_h = 0

for i in range(N):
    max_h = max(max_h, max(area[i]))
    min_h = min(min_h, min(area[i]))

def dfs(x, y, h):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if visited[x][y] == 0:
        if area[x][y] > h:
            visited[x][y] = 1
            dfs(x - 1, y, h)
            dfs(x, y - 1, h)
            dfs(x + 1, y, h)
            dfs(x, y + 1, h)
            return True
    return False

ans = 0
count = 0
for i in range(max_h + 1):
    visited = [[0] * N for _ in range(N)]
    count = 0
    for j in range(N):
        for k in range(N):
            if area[j][k] > i and visited[j][k] == 0:
                count += 1
                dfs(j, k, i)
    ans = max(ans, count)

print(ans)