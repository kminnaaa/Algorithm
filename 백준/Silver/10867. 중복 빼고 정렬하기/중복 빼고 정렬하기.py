# 백준 10867

N = int(input())
arr = []

arr = set(map(int, input().split()))
arr = sorted(arr)

print(*arr)