import sys
input = sys.stdin.readline

N = int(input())

location = []
for _ in range(N):
    A, B = map(int, input().split())
    location.append([A,B])

location.sort()

s = location[0][0]
e = location[0][1]
length = (e - s)

# 완전히 겹치면 합산하면 안됨
    # --> 다음번 시작하는 애랑 끝나는 애 둘 다 e보다 작을 때
# 일부만 겹치면 안 겹치는 부분만 합산
    # --> 다음번 시작하는 애가 e보다 작고, 다음번 끝나는 애가 e보다 큼
for i in range(1, N):
    if location[i][0] <= e and location[i][1] <= e:
        continue
    elif location[i][0] < e and location[i][1] > e:
        length += (location[i][1] - e)
        s, e = location[i][0], location[i][1]
    else:
        length += (location[i][1] - location[i][0])
        e = location[i][1]
        s = location[i][0]

print(length)