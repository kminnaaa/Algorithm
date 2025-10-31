# 백준 5397 - 키로거

"""
스택 .. . 
"""

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    keys = input().strip()
    left, right = [], []

    for k in keys:
        # 커서 왼쪽으로 이동
        if k == '<':
            # 왼쪽 스택 비지 않았다면
            if left:
                right.append(left.pop())    # pop해서 오른쪽 스택에 추가
        # 커서 오른쪽으로 이동
        elif k == '>':
            # 오른쪽 스택 비지 않았다면
            if right:
                left.append(right.pop())    # 왼족에 추가
        # 커서 왼쪽 글자 삭제
        elif k == '-':
            # 왼쪽 마지막 글자 pop
            if left:
                left.pop()
        # 커서 기준 왼쪽에 글자 추가 = 왼쪽 스택에 추가
        else:
            left.append(k)

    # 오른쪽 스택 뒤집어서 왼쪽 뒤에 추가
    left.extend(reversed(right))
    print(''.join(left))