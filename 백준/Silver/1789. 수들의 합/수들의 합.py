# 백준 1789

S = int(input())
num = int(S**(1/2))

while num*(num+1)/2 <= S:
    num += 1

print(num - 1)