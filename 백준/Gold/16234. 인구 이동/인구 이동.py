"""
국경 공유하는 두 나라의 인구 차이가 L 이상 R 이하라면,
공유하는 국경선 하루동안 오픈

  국경 공유 : x 좌표나 y 좌표 중 하나라도 같으면
  인구 차이 L 이상 R 이하라면

국경선 모두 열렸다면 인구 이동 시작

국경선 열려있어 인접한 칸 이용해 이동할 수 있으면, 그 나라를 '연합'

연합 이루고 있는 각 칸 인구수 = (연합 인구수)/(연합 이루는 칸의 개수), 소수점은 절사
  = 이렇게 만들어 줄 때까지 (더 이상 이동 없을 때까지) 반복
연합 해체하고, 모든 국경선 닫는다

union : 같은 연합인지 체크 + 방문 여부 체크
   연합국 저장? 인구 수 계산을 위한 배열
united : 한 연합에 속한 모든 나라 좌표 담는 리스트 -> bfs 끝나고 인구 분배할 리스트
  > 차이를 정확히는 모르겠음
"""
from collections import deque

N, L, R = map(int, input().split())

country = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

def bfs(x, y, index):
    united = []     # 현재 연합에 포함된 국가 좌표
    united.append((x, y))

    queue = deque()
    queue.append((x, y))

    union[x][y] = index
    population = country[x][y]  # 연합 총 인구 수
    count = 1   # 연합 국가 수

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내 + 아직 방문 안 했을 경우
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                if L <= abs(country[nx][ny] - country[x][y]) <= R:
                    queue.append((nx, ny))
                    union[nx][ny] = index
                    population += country[nx][ny]
                    count += 1
                    united.append((nx, ny))

    for i, j in united:
        country[i][j] = population // count
    return count


total_count = 0

while True:
    union = [[-1] * N for _ in range(N)]
    index = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1
    if index == N * N:
        break
    total_count += 1

print(total_count)