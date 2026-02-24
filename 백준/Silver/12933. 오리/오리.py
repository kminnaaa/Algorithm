sound = input().strip()

count = {'q': 0, 'u': 0, 'a': 0, 'c': 0, 'k': 0}
ducks = 0
flag = True

for s in sound:
    if s == 'q':
        if count['k'] > 0:
            count['k'] -= 1
        else:
            ducks += 1
        count['q'] += 1
            
    elif s == 'u':
        if count['q'] > 0:
            count['q'] -= 1
            count['u'] += 1
        else:
            flag = False; break
                
    elif s == 'a':
        if count['u'] > 0:
            count['u'] -= 1
            count['a'] += 1
        else:
            flag = False; break
                
    elif s == 'c':
        if count['a'] > 0:
            count['a'] -= 1
            count['c'] += 1
        else:
            flag = False; break
                
    elif s == 'k':
        if count['c'] > 0:
            count['c'] -= 1
            count['k'] += 1
        else:
            flag = False; break
        
    else:
        flag = False; break

if not flag or count['q'] > 0 or count['u'] > 0 or count['a'] > 0 or count['c'] > 0:
    print(-1)
else:
    if ducks > 0:
        print(ducks)
    else:
        print(-1)