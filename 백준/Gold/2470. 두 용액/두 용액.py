# 백준 2470

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N-1

min_val = abs(arr[left] + arr[right])
answer = [arr[left], arr[right]]

while left < right:
    total = arr[left] + arr[right]
  
    if abs(total) < min_val:
        min_val = abs(total)
        answer = [arr[left], arr[right]]
        if min_val == 0:
            break

    if total < 0:
        left += 1
    else:
        right -= 1

# 결과 출력
print(answer[0], answer[1])
