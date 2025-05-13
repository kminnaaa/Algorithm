# 백준 7795

import bisect
import sys

for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    A = sorted(list(map(int, sys.stdin.readline().split())))
    B = sorted(list(map(int, sys.stdin.readline().split())))
    count = 0
    for a in A:
        count += (bisect.bisect_left(B, a))
    print(count)