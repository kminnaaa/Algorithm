"""
입력 어떻게?

while input: 하면 무한루프
"""

import sys

count = {}

while True:
    input = sys.stdin.readline().strip()

    # 입력이 아닐 경우 break
    if not input:
        break

    # 딕셔너리에 추가하거나, 기존 요소 +1
    if input in count:
        count[input] += 1
    else:
        count[input] = 1

# 딕셔너리 정렬 후 출력 조건 맞춰서 출력
for j in sorted(count.keys()):
    print(j, f"{(count[j] / sum(count.values())) * 100:.4f}")