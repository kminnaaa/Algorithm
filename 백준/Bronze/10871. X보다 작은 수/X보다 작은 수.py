import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for n in A:
    if n < X: ans.append(n)

print(*ans)