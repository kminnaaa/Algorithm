import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    P = input().strip()
    N = int(input())
    arr_input = input().strip()
    
    if arr_input == '[]':
        arr = deque()
    else:
        arr = deque(arr_input[1:-1].split(','))

    r_flag = False

    for order in P:
        if order == 'R':
            r_flag = not r_flag
        elif order == 'D':
            if not arr:
                print('error')
                break
            if r_flag:
                arr.pop()
            else:
                arr.popleft()
    else:
        if r_flag:
            arr.reverse()
        print('[' + ','.join(arr) + ']')