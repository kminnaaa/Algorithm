# 백준 18310

N = int(input())

location = list(map(int, input().split()))
location.sort()

print(location[(N-1)//2])