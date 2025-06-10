N = int(input())
coins = list(map(int, input().split()))
coins.sort()

money = 1
for coin in coins:
  if coin > money:
    break
  money += coin

print(money)