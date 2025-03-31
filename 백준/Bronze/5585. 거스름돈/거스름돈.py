# 백준 5585

num = int(input(""))
N = 1000 - num
count = 0
coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    count += N // coin
    N %= coin

print(count)