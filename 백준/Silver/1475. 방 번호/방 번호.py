"""
0~9 한 세트, 6 <-> 9는 호환 가능
각 숫자 개수 세기 -> 6, 9 처리는?
남아있으면 세트 내에서 처리하고 아니면 새 세트 
arr[6] arr[9] 비교해서, 더 작은 쪽 증가
"""

N = input()

arr = [0] * 10

for num in N:
  if int(num) == 6 or int(num) == 9:
    if arr[6] <= arr[9]:
      arr[6] += 1
    else:
      arr[9] += 1
  else:
    arr[int(num)] += 1
  
print(max(arr))