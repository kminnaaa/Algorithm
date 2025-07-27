"""
남자 1 여자 2
남자: 자기 번호의 배수인 번호의 스위치 상태 바꿈
여자: 자기가 받은 수와 같은 번호의 스위치 중심,
      1. 좌우 대칭
      2. 가장 많은 스위치 포함하는 구간 내 스위치 상태 바꿈
"""

N = int(input())
status = [-1] + list(map(int, input().split()))
student = int(input())

for i in range(student):
  sex, num = map(int, input().split())
  if sex == 1:
    for j in range(num, N + 1, num):
      if status[j] == 0:
        status[j] = 1
      else:
        status[j] = 0
  elif sex == 2:
    if status[num] == 0:
      status[num] = 1
    else:
      status[num] = 0
    left, right = num - 1, num + 1
    while left > 0 and right <= N and status[left] == status[right]:
      if status[left] == 0:
        status[left], status[right] = 1, 1
      else:
        status[left], status[right] = 0, 0
      left -= 1
      right += 1

for k in range(1, N+1):
  print(status[k], end=" ")
  if k % 20 == 0:
    print()