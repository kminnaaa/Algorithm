# 백준 2839

N = int(input())
count = 0

while True:
    if N % 5 == 0:
        count += N // 5
        break
    elif N % 5 != 0:
        N -= 3
        count += 1

    if N < 0:
        count = -1
        break

print(count)