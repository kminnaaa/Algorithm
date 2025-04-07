# 백준 11399

N = int(input())
waiting = list(map(int, input().split()))

waiting.sort()
answer = 0

for i in range(0, N):
    answer += waiting[i] * (N-i)

print(answer)