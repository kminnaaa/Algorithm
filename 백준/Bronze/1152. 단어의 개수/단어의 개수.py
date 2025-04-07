# 백준 1152

string = input()
answer = 0
string = string.strip()


if string == '':
    answer = 0
else:
    answer = string.count(' ') + 1
        

print(answer)