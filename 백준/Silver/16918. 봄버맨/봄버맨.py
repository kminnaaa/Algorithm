"""
폭탄 있는 칸 : 3초 지난 후 폭발
  > 폭탄 있던 칸 + 인접 상하좌우도 빈칸 (여기 폭탄 있을 경우 폭발 x 빈칸)

폭탄 설치 > 1초 휴식 > 폭탄 없는 모든 칸에 폭탄 설치 > 초기에 설치한 폭탄 모두 폭발 
 > 3 4 반복

 케이스 분기 어떻게 ?

 2초에 설치 (전체가 폭탄이 됨),
 3초에 폭발 (3초 전에 설치된 것, 십자),
 4초에 설치 (격자 전체 폭탄),
 5초에 폭발 (전체가 다 폭발)
"""

import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N -= 1  # 1초는 아무 것도 하지 않음

while N:
    bomb = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'O':
                bomb.append((i, j))

    # 모든 칸에 폭탄 설치
    for i in range(R):
        for j in range(C):
            graph[i][j] = 'O'

    N -= 1
    if N == 0:
        break

    # 3초 전에 설치된 폭탄 폭발
    for a, b in bomb:
        graph[a][b] = '.'
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < R and 0 <= y < C:
                graph[x][y] = '.'

    N -= 1

for row in graph:
    print(''.join(row))
