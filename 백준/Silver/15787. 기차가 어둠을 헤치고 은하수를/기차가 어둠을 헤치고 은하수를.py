# N : 기차의 번호 (1번, 2번, ..., N번)
# M : 명령의 개수
N, M = map(int, input().split())
trains = [[0] * 20 for _ in range(N)]

for _ in range(M):
    order = list(map(int, input().split()))
    order_type = order[0]
    train_num = order[1]

    if order_type == 1:
        if trains[train_num-1][order[2]-1] == 0:
            trains[train_num-1][order[2]-1] = 1
    elif order_type == 2:
        if trains[train_num-1][order[2]-1] == 1:
            trains[train_num-1][order[2]-1] = 0
    elif order_type == 3:
        if trains[train_num-1][19] == 1:
            trains[train_num-1][19] = 0
        for i in range(18, -1, -1):
            if trains[train_num-1][i] == 1:
                trains[train_num-1][i+1] = 1
                trains[train_num-1][i] = 0              
    elif order_type == 4:
        if trains[train_num-1][0] == 1:
            trains[train_num-1][0] = 0
        for i in range(1, 20):
            if trains[train_num-1][i] == 1:
                trains[train_num-1][i-1] = 1
                trains[train_num-1][i] = 0

ans = set()
for t in trains:
    ans.add(tuple(t))

print(len(ans))