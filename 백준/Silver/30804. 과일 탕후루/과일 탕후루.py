"""
앞쪽, 뒤쪽에서 과일 빼서 두 종류 이하 과일만 남기기로
이렇게 만든 탕후루 중 과일 개수 최대

?
"""

N = int(input())
fruits = list(map(int, input().split()))

start = 0
ans = 0
count = {}

for end in range(N):
    current = fruits[end]

    if current not in count:
        count[current] = 1
    else:
        count[current] += 1
    
    while len(count) > 2:
        left = fruits[start]
        count[left] -= 1

        if count[left] == 0:
            del count[left]
        start += 1
    
    tmp = end - start + 1
    ans = max(ans, tmp)

print(ans)