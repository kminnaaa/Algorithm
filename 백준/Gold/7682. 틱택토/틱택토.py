"""
한줄이 한판 (3x3)
X > O X > O 순서
가로 세로 대각선으로 3칸 : 즉시 끝
판 가득 차도 끝
가능한 최종 상태인지 ?

조건..
3칸 채워서 승리로 끝나거나 / 보드 꽉 차서 끝나거나

2. X 승리 : 홀수번째 = Y + 1개
   Y 승리 : 짝수번째 = X + 1개
3. 보드 꽉 찬 경우 = X 5개 O 4개

1. ** 항상 X가 한 개 더 많아야 한다**
"""

result = []

def check_win(board, player):
    for i in range(3):
        # 가로
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # 세로
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
        # 대각선 \
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        # 대각선 /
        if board[0][2] == board [1][1] == board [2][0] == player:
            return True
    return False

while True:
    s = input().strip()
    if s=="end":
        break

    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(s[i*3 + j])
        board.append(row)

    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    x_win = check_win(board, 'X')
    o_win = check_win(board, 'O')

    # 개수 안맞는 경우 : O가 더 많거나, X와 차이 1보다 크거나
    if o_count > x_count or x_count > o_count + 1:
        result.append("invalid")
    # 둘 다 이긴 경우
    elif x_win and o_win:
        result.append("invalid")
    # X가 이겼고, 개수 1 더 많은 경우(홀수)
    elif x_win and x_count == o_count + 1:
        result.append("valid")
    # O가 이겼고, 개수 같은 경우(짝수)
    elif o_win and x_count == o_count:
        result.append("valid")
    # 꽉 찬 경우
    elif not x_win and not o_win and x_count + o_count == 9:
        result.append("valid")
    else:
        result.append("invalid")

for i in result:
    print(i)