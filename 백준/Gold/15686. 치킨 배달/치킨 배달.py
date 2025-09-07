"""
0 : 빈칸, 1 : 집, 2 : 치킨집
도시의 치킨 거리 최소로 만드는 M개의 조합, 이때의 도시의 치킨거리 출력

조합으로 M개 골라서 각각 거리 구하고 최소인 경우 구하기?

chickens = [(x, y) for x, y in info if info[x][y] == 2]
houses = [(x, y) for x, y in info if info[x][y] == 1]
  ValueError: too many values to unpack (expected 2)
"""
import sys
from itertools import combinations

N, M = map(int, input().split())

houses = []
chickens = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            houses.append((i, j))
        elif row[j] == 2:
            chickens.append((i, j))

city_chicken_dist = 1e9

for com in combinations(chickens, M):
    city_dist = 0
    for x, y in houses:
        city_dist += min(abs(x - a) + abs(y - b) for a, b in com)
    city_chicken_dist = min(city_chicken_dist, city_dist)

print(city_chicken_dist)