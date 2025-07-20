"""
입력
제일 바깥 for : T (별개 케이스)
>
M, N(가로, 세로)으로 그래프 초기화
>
그다음 for : K번
>
배추 위치 X, Y 주어짐

0은 빈땅, 1은 배추 심어진 땅


인접해있는 배추들이 몇 군데에 퍼져 있는지..

x, y 순서...................
"""
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
  if x <= -1 or x >= M or y <= -1 or y >= N:
    return False
  
  if graph[y][x] == 1:
    graph[y][x] = -1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  
  return False

T = int(input())
result = []

for _ in range(T):
  M, N, K = map(int, input().split())
  graph = [[0] * M for _ in range(N)]
  for _ in range(K):
    a, b = map(int, input().split())
    graph[b][a] = 1

  temp = 0
  for y in range(M):
    for x in range(N):
      if dfs(y, x) == True:
        temp += 1
  result.append(temp)

for i in range(T):
  print(result[i])