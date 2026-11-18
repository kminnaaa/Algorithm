from itertools import combinations

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(1, N):
        com = combinations(arr, i)

        for pair in com:
            if sum(pair) == K:
                cnt += 1
    
    print(f"#{tc} {cnt}")