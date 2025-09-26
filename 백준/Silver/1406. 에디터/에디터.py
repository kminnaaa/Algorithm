"""
왼쪽 오른쪽 구분 어떻게 처리?
  > 스택 두개**
"""

import sys
input = sys.stdin.readline

left = list(input().rstrip())   # 초기 문자열
right = []

M = int(input())
for _ in range(M):
    cmd = input().split()
    # 명령어가 L이고, 왼쪽 스택 비어있지 않다면, 마지막 문자 pop > right
    if cmd[0] == 'L' and left:
        right.append(left.pop())
    # 명령어가 D이고 오른쪽 스택 비어있지 않다면, 마지막 문자 pop > left
    elif cmd[0] == 'D' and right:
        left.append(right.pop())
    # 왼쪽 스택 비어있지 않다면 pop
    elif cmd[0] == 'B' and left:
        left.pop()
    # 왼쪽 스택에 push
    elif cmd[0] == 'P':
        left.append(cmd[1])
# 오른쪽 스택은 뒤에서부터 출력
print(''.join(left + right[::-1]))