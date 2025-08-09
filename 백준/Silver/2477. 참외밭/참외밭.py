"""
동 1
서 2
남 3
북 4

임의의 꼭짓점에서 출발,
반시계방향으로 돌면서 지나는 변의 방향과 길이

1이나 2는 가로변
3이나 4는 세로변

12, 34 중에 가장 큰애들이 틀이고
작은 사각형 어떻게 구하ㅁ ?

제일 긴 거에 붙어있으면 큰 사각형 일부
  > 어떻게? 제일긴거 인덱스 양옆 (+1, -1)
     ** 이때 %6 해줘야 안전
"""

K = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

width, width_idx = 0, 0
height, height_idx = 0, 0

for i in range(6):
    dir, length = arr[i]
    if dir == 1 or dir == 2:
        if length > width:
            width = length
            width_idx = i
    else:
        if length > height:
            height = length
            height_idx = i

w = abs(arr[(width_idx - 1) % 6][1] - arr[(width_idx + 1) % 6][1])
h = abs(arr[(height_idx - 1) % 6][1] - arr[(height_idx + 1) % 6][1])

area = (width * height) - (w * h)
print(area * K)