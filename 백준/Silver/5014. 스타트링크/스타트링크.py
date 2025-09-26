"""
총 F층
현재 위치 : S층
도착지 : G층

U : 위로 U층 가는 버튼
D : 아래로 D층 가는 버튼

최소 거리.. bfs

"""
from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [False] * (F + 1)
q = deque()
q.append((S, 0))
visited[S] = True

flag = False
while q:
    floor, count = q.popleft()

    if floor == G:
        print(count)
        flag = True
        break

    for nf in [floor - D, floor + U]:
        if 1 <= nf <= F and not visited[nf]:
            visited[nf] = True
            q.append((nf, count + 1))

if not flag:
    print("use the stairs")