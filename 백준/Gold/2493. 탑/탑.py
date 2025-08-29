"""
N개, 높이 서로 다른 탑 왼쪽 ~ 오른쪽 차례로 세움

레이저 : 오른쪽 > 왼쪽
레이저 쐈을 때, 레이저 첫번째로 맞는 탑 번호
  = 왼쪽에 있는 탑 중에 더 높은 거
  왼쪽에서부터 탐색하면서 넣고, 높이 낮으면 빼고?

자료구조.. 스택?

"""

import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
stack = []
result = [0] * N

for i in range(0, N):
    while stack:
        # 현재 높이가 더 높을 경우, 전파 못 맞으니까 pop
        if towers[i] > stack[-1][1]:
            stack.pop()
        # 현재 높이보다 높을 경우, 전파 맞을 수 있으니까 맞는 첫 번째 탑 답에 추가
        else:
            result[i] = stack[-1][0]
            break
    stack.append((i + 1, towers[i]))    # 번호 1부터니까 + 1
print(*result)