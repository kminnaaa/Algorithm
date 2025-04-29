# 백준 2470

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N-1

answer = abs(arr[left] + arr[right])
value = [arr[left], arr[right]]


while left < right:
    left_val = arr[left]
    right_val = arr[right]

    sum = left_val + right_val
  
    if abs(sum) < answer:
        answer = abs(sum)
        value = [left_val, right_val]
        if answer == 0:
          break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(value[0], value[1])