"""
홀 > 짝

동일 선분 x, 선분 교차는 o
사이클 완성하면 종료
  = C에 속한 임의의 선분의 한 끝점에서 출발하여 모든 선분을 한 번씩만 지나서 출발점으로 되돌아올 수 있다

union find
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
parent = [x for x in range(N)]

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent_x = find(x)
    parent_y = find(y)
    if parent_x < parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y

result = 0
for i in range(1, M+1):
    x, y = map(int, input().split())
    if find(x) == find(y):
        result = i
        break
    union(x, y)
    
print(result)