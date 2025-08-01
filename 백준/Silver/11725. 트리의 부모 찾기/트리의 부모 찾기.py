"""
1: 4, 6 이런 식으로 해쉬로 저장
양방향 저장

노드 개수만큼 만들어주고,
부모 노드 값 저장

recursion 에러 > 리밋 늘려줌
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for i in range(N+1)]

def dfs(n):
    for i in graph[n]:
        if visited[i] == 0:
            visited[i] = n
            dfs(i)

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

dfs(1)

for i in range(2, N+1):
    print(visited[i])