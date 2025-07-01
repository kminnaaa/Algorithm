move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1],
        'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

k, s, count = input().split()
count = int(count)
king = list(map(int, [ord(k[0]) - 64, k[1]]))
stone = list(map(int, [ord(s[0]) - 64, s[1]]))

for i in range(count):
  direction = input()
  dx, dy = move[direction]
  
  nx = king[0] + dx
  ny = king[1] + dy

  if 1 <= nx <= 8 and 1 <= ny <= 8:
    if nx == stone[0] and ny == stone[1]:
      if 1 <= stone[0] + dx <= 8 and 1 <= stone[1] + dy <= 8:
        stone = [stone[0] + dx, stone[1] + dy]
        king = [nx, ny]
    else:
      king = [nx, ny]

print(f'{chr(king[0] + 64)}{king[1]}')
print(f'{chr(stone[0] + 64)}{stone[1]}')
