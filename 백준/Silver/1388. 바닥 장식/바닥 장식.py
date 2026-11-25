N, M = map(int, input().split())
room = [list(input().strip()) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if room[i][j] == '-':
            if j == 0 or room[i][j - 1] != '-':
                cnt += 1
        elif room[i][j] == '|':
            if i == 0 or room[i - 1][j] != '|':
                cnt += 1      
        
print(cnt)