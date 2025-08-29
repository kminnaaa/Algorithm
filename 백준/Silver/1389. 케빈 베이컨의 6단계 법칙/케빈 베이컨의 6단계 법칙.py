"""
양방향 저장, 경로 +
"""

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [-1] * (N+1)
    visited[start] = 0
    q = deque([start])

    while q:
        # 현재 탐색
        c = q.popleft()
        # 현재 탐색 대상과 연결된 모든 친구 확인
        for n in graph[c]:
            # 아직 방문하지 않은 경우
            if visited[n] == -1:
                # 거리 갱신
                visited[n] = visited[c] + 1
                q.append(n)
    return sum(visited[1:])     # 1 ~ N까지 거리 +

minimum = 1e9
ans = 0

# 1번부터 N번까지 돌면서 탐색
for person in range(1, N+1):
    total = bfs(person)
    # 최소값 찾기
    if total < minimum:
        minimum = total
        ans = person

print(ans)