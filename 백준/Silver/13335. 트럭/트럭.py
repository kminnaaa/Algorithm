"""
n: 트럭 수
w: 다리 길이
L: 최대 하중

weight은 각각 N+1번 트럭의 무게
"""

from collections import deque

n, w, L = map(int, input().split())  # 트럭 수, 다리 길이, 하중
weight = list(map(int, input().split()))

bridge = deque([0] * w)  # 다리 상태 초기화
time = 0
current_weight = 0

while bridge:
    time += 1
    # 가장 왼쪽 하나 -
    current_weight -= bridge.popleft()

    # 트럭 남아있는지,
    if weight:
        # 다음 트럭 다리에 올릴 수 있는지 확인
        if current_weight + weight[0] <= L:
            # 가능하면, 다리에 트럭 올림
            truck = weight.pop(0)
            bridge.append(truck)
            current_weight += truck
        # 못 올리면 뒤에 한칸 추가 (현재 다리위 트럭 전진)
        else:
            bridge.append(0)

print(time)