"""
첫번째 : 오름차순 (0 < 1 < 2 < 3)

뒤에서부터 바뀌니까 뒤에서부터 비교?
원래는 앞 < 뒤 여야 하고
앞 > 뒤일 경우 ?



"""

N = int(input())
num = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    if num[i - 1] > num[i]:
        for j in range(N - 1, 0, -1):
            if num[i - 1] > num[j]:
                num[i - 1], num[j] = num[j], num[i - 1]
                num = num[:i] + list(reversed(num[i:]))
                print(*num)
                exit()
print(-1)