import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
field = [list(input().strip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, distance):
    # 도착지에 도달 + 거리가 K
    # 도착점: (0, C-1)
    if x == 0 and y == C - 1:
        return 1 if distance == K else 0
    
    if distance >= K:
        return 0
    
    # dfs 돌리면서
    # 방문처리 --> .인 것만 방문 가능 --> 방문 후 T로 바꾸기 ?
    # 근데 모든 가짓수 찾아야 하니까 T로 바꾼 상태에서 dfs(nx, ny) 호출하고
    # 다시 .으로 바꿔 놓고 종료 ?

    field[x][y] = 'T'
    count = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C and field[nx][ny] == '.':
            count += dfs(nx, ny, distance + 1)
            
    field[x][y] = '.'
    
    return count

# 출발점: (R-1, 0), 시작 거리: 1
print(dfs(R-1, 0, 1))