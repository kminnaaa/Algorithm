"""
흑 1
백 2
빈칸 0

승부 결과
가장 왼쪽/가장 위쪽 돌 위치 (가로줄 번호 세로줄 번호)

**
6개인 경우 체크해야 함

"""


import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, -1, 1]
dy = [1, 0, 1, 1]

# 가로 세로 / \
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            target = board[x][y]
            
            for i in range(4):
                count = 1
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 범위 체크, 다음 돌이 현재 돌과 같은 색인지
                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == target:
                    count += 1

                    # 5개 다 찼을 때, 6개가 아니어야 승리
                    if count == 5:
                        # target의 이전 돌이 같은 색인지
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == target:
                            break
                        # 현재 돌의 다음 돌이 같은 색인지
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == target:
                            break

                        print(target)
                        print(x + 1, y + 1)
                        exit(0)
                    
                    # 다음 방향
                    nx += dx[i]
                    ny += dy[i]
                    
print(0)
