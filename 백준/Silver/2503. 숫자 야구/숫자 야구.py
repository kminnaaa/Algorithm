"""
같은 숫자, 같은 위치 : 스트라이크
다른 위치 : 볼
"""

from itertools import permutations

N = int(input())
questions = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for p in permutations(range(1, 10), 3):
    flag = 1
    for question, strike, ball in questions:
        s = 0
        b = 0
        q = list(map(int, str(question)))
        for j in range(3):
            if q[j] == p[j]:
                s += 1
            elif q[j] in p:
                b += 1
        if s != strike or b != ball:
            flag = 0
            break
    if flag == 1:
        ans += 1

print(ans)