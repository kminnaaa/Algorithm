N = int(input())

count = {}
best = []

for i in range(N):
  tmp = input()
  if tmp not in count:
    count[tmp] = 1
  else:
    count[tmp] += 1

ans = max(count.values())

for book in count:
  if ans == count[book]:
    best.append(book)

best.sort()
print(best[0])