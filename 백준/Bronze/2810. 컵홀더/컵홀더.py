# 백준 2810
"""
`S`S`S`S` s만 있으면 N

`LL`S`S`
`LL`S`S`S` LL 하나 있으면 N

`S`LL`LL`S` 5개 (N = 6)
`S`LL`LL`S`S` 6개 (N = 7)
LL 두개면 N - 1

`S`LL`LL`S`LL`S` 7개 (N = 9)
`S`LL`LL`LL`S` 6개 (N = 8)
LL 세개면 N - 2

if countLL <= 1: N
else: N - (countLL - 1)
"""

N = int(input())
seat = input()

countLL = seat.count('LL')

if countLL <= 1:
    print(N)
else:
    print(N - (countLL - 1))