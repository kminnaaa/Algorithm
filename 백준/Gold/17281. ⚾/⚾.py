from itertools import permutations

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]

players = [2, 3, 4, 5, 6, 7, 8, 9]
maximum = 0

for perm in permutations(players):
    order = list(perm[:3]) + [1] + list(perm[3:])
    # 홈(점수), 1루, 2루, 3루
    base = [0, 0, 0, 0]
    next = 0

    for inning in innings:
        # 이닝마다 아웃, 루상 주자 초기화
        out = 0
        base[1], base[2], base[3] = 0, 0, 0

        while out < 3:
            player = order[next]

            if inning[player - 1] == 0:
                out += 1
            elif inning[player - 1] == 1:
                base[0] += base[3]
                base[3], base[2], base[1] = base[2], base[1], 1
            elif inning[player - 1] == 2:
                base[0] += base[3] + base[2]
                base[3], base[2], base[1] = base[1], 1, 0
            elif inning[player - 1] == 3:
                base[0] += base[3] + base[2] + base[1]
                base[3], base[2], base[1] = 1, 0, 0
            elif inning[player - 1] == 4:
                base[0] += base[3] + base[2] + base[1] + 1
                base[3], base[2], base[1] = 0, 0, 0
            
            # 0 ~ 8
            next = (next + 1) % 9
    
    maximum = max(maximum, base[0])

print(maximum)