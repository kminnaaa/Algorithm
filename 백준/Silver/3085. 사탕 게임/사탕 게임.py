N = int(input())
board = [list(input().strip()) for _ in range(N)]

def find_longest():
    length = []
    max_length = 0

    # 행
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if board[i][j] == board[i][j+1]:
                cnt += 1
            else:
                max_length = max(max_length, cnt)
                cnt = 1
        max_length = max(max_length, cnt)

    # 열
    for j in range(N):
        cnt = 1
        for i in range(N-1):
            if board[i][j] == board[i+1][j]:
                cnt += 1
            else:
                max_length = max(max_length, cnt)
                cnt = 1
        max_length = max(max_length, cnt)
            
    return max_length


# 인접한 두칸 : x축이나 y축 중 하나 같은 것
# 인접한 두칸 선택 > 문자 서로 교환 (아마도 한번만 이루어지는 듯)
# NxN (0~N-1) 배열에서, x축이 같거나 y축이 같거나
arr = []
for i in range(N):
    for j in range(N-1):
        # 가로 인접
        # [i][j]랑 [i][j+1]이랑 교환
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        arr.append(find_longest())
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        # 세로 인접
        # [i][j]랑 [i+1][j]랑 교환
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
        arr.append(find_longest())
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(max(arr))
# 같은 색으로 이루어져 있는 가장 긴 연속 부분 (하나만, 행/열) 선택 후 모두 먹음
# 먹을 수 있는 사탕의 최대 개수