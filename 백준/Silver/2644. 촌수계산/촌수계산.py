"""
촌수 계산해야 하는 서로 다른 두 번호

부모 - 자식 간 관계 개수 (얘네끼리는 다 1촌)
부모 자식 간 관계 나타내는 두 번호 x, y
x는 뒤에 나오는 y의 부모 번호

양방향으로 저장
a에서 출발해서 b 도착하는 거리 = 촌수
"""

N = int(input())
a, b = map(int, input().split())

graph = [[] for _ in range(N+1)]
M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N+1)
result = []

def dfs(v, n):
    n += 1
    visited[v] = True

    if v == b:
        result.append(n)
    for i in graph[v]:
        if not visited[i]:
            dfs(i, n)

dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)