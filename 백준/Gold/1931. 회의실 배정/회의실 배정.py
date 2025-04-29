# 백준 1931

import sys

N = int(sys.stdin.readline())
time = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time.sort(key=lambda x:(x[1], x[0]))
    
answer = 0
end = 0

for i in range(N):
    if end <= time[i][0]:
        answer += 1
        end = time[i][1]
print(answer)