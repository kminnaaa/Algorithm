"""
꼭짓점이 같은 수면 됨
꼭짓점이 같으려면. 행이 같거나 열이 같거나..

변 길이 기준으로 줄여가면서
flag 쓰면 루프 빠져나가기 복잡 > 함수
1일때.. size가 1까지 작아지면 조건문 내 모든 조건이 동일해짐
"""
import sys
input = sys.stdin.readline

def rectangle(size):
  for j in range(N - size + 1):
    for k in range(M - size + 1):
      if rect[j][k] == rect[j][k + size - 1] == rect[j + size - 1][k] == rect[j + size -1][k + size -1]:
        return True

N, M = map(int, input().split())
rect = [list(input()) for _ in range(N)]

size = min(N, M)

for i in range(size, 0, -1):
  if rectangle(i):
    print(i * i)
    break