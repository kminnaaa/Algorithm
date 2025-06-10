N = int(input())

bag = [5, 3]

count = 0
while N > 0:    # 0이 되면 종료
  if N % 5 == 0:
    count += (N // 5)
    break
  elif N % 5 != 0 and N >= 3:
    N -= 3
    count += 1
  elif N < 3:
    count = -1
    break


print(count)