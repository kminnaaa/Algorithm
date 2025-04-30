# 백준 1764

import sys

input = sys.stdin.readline
N, M = map(int, input().split())

deut = set()
bo = set()

for _ in range(N):
    deut.add(input().strip())
for _ in range(M):
    bo.add(input().strip())

deutbo = sorted(deut & bo)

print(len(deutbo))

for i in deutbo:
    print(i)