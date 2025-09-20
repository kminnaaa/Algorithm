"""
매칭 가능한 방 없으면 새로운 방 생성 > 입장
(처음 입장한 플레이어 레벨 기준 +-10까지 입장 가능)

입장 가능한 방 있다면 입장시키고, 정원 모두 찰때까지 대기
  - 입장 가능한 방 여러개면 먼저 생성된 방에 입장
방의 정원이 모두 차면 게임 시작

모든 방에 대해, 게임 시작 여부와 방에 있는 플레이어 출력
방은 생성된 순서대로 출력
플레이어 정보는 닉네임 사전순
"""

p, m = map(int, input().split())
players = []
rooms = []

for _ in range(p):
    l, n = input().split()
    players.append([int(l), n])

for lev, name in players:
    flag = 0
    for i in range(len(rooms)):
        if rooms[i][0][0] - 10 <= lev <= rooms[i][0][0] + 10 and len(rooms[i]) < m:
            rooms[i].append([lev, name])
            flag = 1
            break
    if flag == 0:
        rooms.append([[lev, name]])

for i in range(len(rooms)):
    if len(rooms[i]) == m:
        print('Started!')
    else:
        print('Waiting!')
    for lev, name in sorted(rooms[i], key=lambda x: x[1]):
        print(lev, name)