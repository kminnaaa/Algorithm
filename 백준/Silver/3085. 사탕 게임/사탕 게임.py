"""
사탕의 색이 다른 인접한 두 칸을 고른다
고른 칸에 들어있는 사탕을 서로 교환
모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)
그 사탕을 모두 먹는다.

상근이가 먹을 수 있는 사탕의 최대 개수

교환할 수 있는 칸 다 교환해 보고 거기서 최댓값 구하기?
탐색은 오른쪽 아래로
같은 칸끼리 바꿔도 결과 똑같으니까 그냥 바꿔도 ok
일단 바꿔보고 다시 되돌려 놓기 max만 구하면 되니까
"""
import sys
input = sys.stdin.readline

N = int(input())
board = [list(input()) for _ in range(N)]

def count(board):
    maximum = 0
    for i in range(N):
        row = 1
        col = 1
        for j in range(1, N):
            # 오른쪽 탐색
            if board[i][j] == board[i][j - 1]:
                row += 1
            else:
                row = 1
            maximum = max(maximum, row)

            # 아래로 탐색
            if board[j][i] == board[j - 1][i]:
                col += 1
            else:
                col = 1
            maximum = max(maximum, col)
    return maximum

ans = 0

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            ans = max(ans, count(board))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        # 아래쪽이랑 바꾸기
        if i + 1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            ans = max(ans, count(board))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)