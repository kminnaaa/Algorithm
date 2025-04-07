# 백준 10866

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
Deque = deque()

for i in range(N):
    order = input().split()

    if order[0] == 'push_front':
        Deque.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        Deque.append(int(order[1]))
    elif order[0] == 'pop_front':
        if not Deque: print(-1)
        else:
            print( Deque.popleft())
    elif order[0] == 'pop_back':
        if not Deque: print(-1)
        else:
            print(Deque.pop())
    elif order[0] == 'size':
        print(len(Deque))
    elif order[0] == 'empty':
        if not Deque: print(1)
        else: print(0)
    elif order[0] == 'front':
        if not Deque: print(-1)
        else: print(Deque[0])
    elif order[0] == 'back':
        if not Deque: print(-1)
        else: print(Deque[-1])