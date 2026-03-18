# 백준 14889
from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

"""
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 
에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다.
Sij는 Sji와 다를 수도 있으며,
i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

S[0][1] = 1 - 1, 2번 같은 팀
S[1][0] = 4

0 1 vs 2 3
1 2 vs 0 3

0 1 2 vs 3 4 5
S01 + S10 + S02 + S20 ... 
0 1 3 vs 2 4 5
"""

candidates = [i for i in range(N)]
arr = list(combinations(candidates, N//2))

answer = float('inf')

# 맨앞에서 하나, 맨뒤에서 하나 고르면 각팀 구성 가능
for team1 in arr:
    # i팀에, N//2명만큼 사람 있고
    team2 = [x for x in candidates if x not in team1]
    
    sum1 = 0
    sum2 = 0
    
    for a, b in combinations(team1, 2):
        sum1 += S[a][b] + S[b][a]
    
    for a, b in combinations(team2, 2):
        sum2 += S[a][b] + S[b][a]
    
    answer = min(answer, abs(sum1 - sum2))

print(answer)