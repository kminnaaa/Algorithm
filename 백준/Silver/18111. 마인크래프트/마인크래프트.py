"""
제거 2초, 쌓는 거 1초
브루트포스  ?  256까지 다 해보는겅가


"""

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]

ans_time = 1e9
ans_height = -1

for i in range(257):
  remove = 0
  add = 0
  for j in range(N):
    for k in range(M):
      diff = field[j][k] - i
      if diff > 0:
        remove += diff
      else:
        add -= diff
  if remove + B >= add:
    time = remove * 2 + add
    if time < ans_time:
      ans_time = time
      ans_height = i
    elif time == ans_time:
      ans_height = max(ans_height, i)

print(ans_time, ans_height)