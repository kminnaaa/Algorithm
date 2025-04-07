# 백준 10773

K = int(input())
num = []
cnt = 1
i = 0

while cnt <= K:
    num.append(int(input()))
    cnt += 1
    if num[i] == 0:
        del num[i-1], num[i-1]
        i -= 2
    i += 1
print(sum(num))