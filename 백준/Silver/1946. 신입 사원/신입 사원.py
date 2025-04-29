# 백준 1946

import sys

t = int(sys.stdin.readline())

for i in range(t):
    
    arr = []
    answer = 1

    N = int(sys.stdin.readline())
    
    for j in range(N):
        a, b = map(int, sys.stdin.readline().split())
        arr.append([a, b])
        
    arr.sort()
    
    std = arr[0][1]
    
    for j in range(1, N):
        if std > arr[j][1]:
            answer += 1
            std = arr[j][1]   
    print(answer)