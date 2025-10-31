N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]

# 끝점이 D를 넘거나, 지름길이 더 길면 버림
shortcuts = [s for s in shortcuts if s[1] <= D and (s[1] - s[0]) > s[2]]

# 거리 배열 - i까지 가는 최소 거리
dist = [i for i in range(D + 1)]  # 기본 도로(1씩 이동)

for i in range(D + 1):
    # 한 칸 전에서 온 경우 (기본 도로)
    if i > 0:
        dist[i] = min(dist[i], dist[i - 1] + 1)

    # 현재 위치(i)에서 출발하는 지름길 탐색
    for s, e, l in shortcuts:
        if s == i and e <= D:
            dist[e] = min(dist[e], dist[s] + l)

print(dist[D])