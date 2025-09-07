"""
1 : 북, 2 : 남, 3 : 서, 4 : 동
W 1, 2 왼쪽부터의 거리, H 3, 4 위쪽으로부터의 거리

최단거리를 구하는 방법

케이스별로? - 동근 위치 예제랑 바뀌면 대처 불가
*** 북쪽에서 시작해서 기준 잡고 시계 방향 > 직선으로 생각
조건 분기 중복 안 되게 하려면 함수로
"""

W, H = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
D = list(map(int, input().split()))

def distance(dir, dist):
    if dir == 1:
        return dist
    elif dir == 4:
        return W + dist
    elif dir == 2:
        return W + H + (W - dist)
    elif dir == 3:
        return W + H + W + (H - dist)

dong = distance(D[0], D[1])
result = 0
for dir, dist in arr:
    shop = distance(dir, dist)
    d_to_s = abs(dong - shop)
    result += min(d_to_s, 2 * (W + H) - d_to_s)

print(result)