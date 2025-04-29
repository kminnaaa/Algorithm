# 백준 1715

import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = sorted([int(input()) for _ in range(n)])
answer = 0

while n > 1:
    sum = 0 
    sum += heapq.heappop(q)
    sum += heapq.heappop(q)
    answer += sum
    heapq.heappush(q, sum)
    n -= 1

print(answer)