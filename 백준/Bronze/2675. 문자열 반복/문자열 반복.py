# 백준 2675

T = int(input())
num = 0

for i in range(T):
    num, string = input().split()
    for i in range(len(string)):
        print(int(num) * string[i], end = '')
    print('')