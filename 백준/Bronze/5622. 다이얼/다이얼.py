# 백준 5622

str = input()
cnt = 0
dial = {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5,
        'MNO': 6,'PQRS': 7, 'TUV': 8, 'WXYZ': 9}

for i in str:
    for j in dial:
        if i in j:
            cnt = cnt + 1 + dial[j]
print(cnt)