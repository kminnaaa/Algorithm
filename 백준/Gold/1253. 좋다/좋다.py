# 백준 1253

N = int(input())
array = list(map(int, input().split()))
array.sort()
cnt =0
for i in range(N):
    goal = array[i]
    left = 0
    right = N - 1
    while left < right:
        sum = array[left] + array[right]
        if sum < goal:
            left += 1
        elif sum > goal:
            right -= 1
        else:
            if left != i and right != i:
                cnt += 1
                break
            if left == i:
                left += 1
            elif right == i:
                right -= 1
print(cnt)