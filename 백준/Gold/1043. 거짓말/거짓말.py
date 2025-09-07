"""
진실을 아는 사람 수, 번호(누군지) : 둘째줄에
셋째줄부터는 각각 별개의  : 오는 사람들 수, 번호

거짓말 해도 되는 파티 최대 개수
truth랑 party에 교집합 있으면 거짓말 불가능 > 교집합 있는 것 개수?
   > 오답
   > 거짓말 말해도 되는 파티에 참여했던 사람이 
    이후 파티에 참여하면 얘도 truth 됨
    > truth부터 다 추가하고나서 교집합 체크 : 오답
"""

from collections import deque

# 사람수, 파티 수
N, M = map(int, input().split())

# 진실 아는 사람 번호
truth = set(map(int, input().split()[1:]))

# 파티 참가자들 번호
parties = [set(map(int, input().split()[1:])) for _ in range(M)]

possible = [True] * M
for _ in range(M):
    for i, p in enumerate(parties):
        if p & truth:
            possible[i] = False
            truth = truth | p

"""
# 오답
for party in parties:
    if set(truth) & set(party):
        for p in party:
            if p not in truth:
                truth.append(p)
"""

print(sum(possible))