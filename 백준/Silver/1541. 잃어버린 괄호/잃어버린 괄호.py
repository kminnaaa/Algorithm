num = input().split('-')

arr = []

for i in num:
  sum = 0
  add = i.split('+')
  for j in add:
    sum += int(j)
  arr.append(sum)

for i in range(1, len(arr)):
  arr[0] -= arr[i]

print(arr[0])