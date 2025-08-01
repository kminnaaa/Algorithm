"""
연결된 집 = 단지, 단지에 번호 붙임
각 단지에 속하는 집의 수 오름차순으로 정렬하여 출력
NxN 지도

입력 어케받음 -> (split() 넣으면 0110으로 되고 아니면 0, 1, 1, 0)

조건 - 단지 수, 아파트 수 각각 세어야 하고 
단지 수는 호출하는 곳에서 세고,(기존과 동일)
아파트 수는 호출받을 때마다 count해서 append

tmp 로컬 에러 > scope 에러 계속 발생 > 횟수 return 하는걸로 수정
"""
N = int(input())
area = [list(map(int, input())) for _ in range(N)]

def dfs(x, y):
    global tmp
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if area[x][y] == 1:
        area[x][y] = 0
        tmp = 1
        tmp += dfs(x - 1, y)
        tmp += dfs(x, y - 1)
        tmp += dfs(x + 1, y)
        tmp += dfs(x, y + 1)
        return tmp
    return False

ans = []
for i in range(N):
    for j in range(N):
        if area[i][j] == 1:
            ans.append(dfs(i, j))


print(len(ans))
ans.sort()
for i in ans:
    print(i)