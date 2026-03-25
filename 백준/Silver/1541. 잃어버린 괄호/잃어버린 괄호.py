tmp = input().split('-')

arr = []

for n in tmp:
    sum = 0
    tmp = n.split('+')
    for m in tmp:
       sum += int(m)
    arr.append(sum)

for i in range(1, len(arr)):
   arr[0] -= arr[i]

print(arr[0])
        