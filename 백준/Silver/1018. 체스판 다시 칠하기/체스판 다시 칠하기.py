import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
answer = 64

start_W = 'WBWBWBWB'
start_B = 'BWBWBWBW'

for _ in range(N):
  board.append(input().strip())

for row in range(N - 7):
  for square in range(M - 7):
    cnt = 0
    for i in range(row, row + 8):
      if i % 2 == 0:
        cnt += sum(1 for a, b in zip(board[i][square:square+8], start_W) if a != b)
      else:
        cnt += sum(1 for a, b in zip(board[i][square:square+8], start_B) if a != b)
    answer = min(answer, cnt)

    cnt = 0
    for i in range(row, row + 8):
      if i % 2 == 0:
        cnt += sum(1 for a, b in zip(board[i][square:square+8], start_B) if a != b)
      else:
        cnt += sum(1 for a, b in zip(board[i][square:square+8], start_W) if a != b)
    answer = min(answer, cnt)

print(answer)
