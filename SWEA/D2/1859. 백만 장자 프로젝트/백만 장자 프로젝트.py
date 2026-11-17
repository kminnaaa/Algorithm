T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    cur_max = 0
    profit = 0
    for p in reversed(price):
        if p < cur_max:
            profit += (cur_max - p)
        if p >= cur_max:
            cur_max = p
    
    print('#{} {}'.format(tc, profit))
