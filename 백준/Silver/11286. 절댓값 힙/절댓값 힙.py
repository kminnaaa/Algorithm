"""
최소 힙 > 파이썬 : heapq

heapq.heappush(heap)
heapq.heappop(heap)

튜플 첫 번째 원소 기준으로 정렬, 같을 경우 두 번째 원소
heappush(heap, (기준1, 기준2, ... , data))
heappop(heap) < 전체 튜플 반환
heappop(heap[1]) < x 반환
"""

import sys
import heapq

input = sys.stdin.readline
heap = []

N = int(input())

for i in range(N):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)