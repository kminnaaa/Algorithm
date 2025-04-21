# 백준 14503

"""
1. (r, c)가 청소되지 않은 경우(0) 현재 칸 청소

2. 현재 칸의 주변 4칸(북, 동, 남, 서) 중 0이 없는 경우, 
    # 북(0) r-1, c > 3
    # 동(1) r, c+1 > 0
    # 남(2) r+1, c > 1
    # 서(3) r, c-1 > 2
2-1. 바라보는 방향 유지하고 한칸 후진 후 1번

3. 현재 칸 주변 4칸 중 0이 있는 경우, 반시계 방향으로 회전 (d+3)%4
3-1. 바라보는 방향 기준, 앞쪽이 0일 경우 한 칸 전진 후 1번

"""

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
answer = 0

while True:
    flag = False
    if room[r][c] == 0:
        room[r][c] = 2
        answer += 1
    for i in range(4):
        d = (d+3) % 4
        nr, nc = r + dir[d][0], c + dir[d][1]
        if room[nr][nc] == 0:
            room[nr][nc] = 2
            answer += 1
            r, c = nr, nc
            flag = True
            break
    if not flag:
        if room[r-dir[d][0]][c-dir[d][1]] == 1:
            print(answer)
            break
        else:
            r, c = r - dir[d][0], c - dir[d][1]