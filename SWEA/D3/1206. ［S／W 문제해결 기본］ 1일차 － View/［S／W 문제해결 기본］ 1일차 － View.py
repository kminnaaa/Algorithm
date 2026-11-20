for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    ans = 0
    for i in range(2, N - 1):
        if buildings[i - 2] < buildings[i] and buildings[i - 1] < buildings[i] and buildings[i + 1] < buildings[i] and buildings[i + 2] < buildings[i]:
            tmp = max(buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2])
            ans += buildings[i] - tmp

    print(f"#{tc} {ans}")