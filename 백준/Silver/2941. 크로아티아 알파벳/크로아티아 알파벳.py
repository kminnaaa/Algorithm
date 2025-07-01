croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

answer = 0
for alphabet in croatian:
  word = word.replace(alphabet, '*')

answer += len(word)
print(answer)

"""
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

answer = 0
arr = []
for alphabet in croatian:
  if alphabet in word:
    arr.append(alphabet)
    answer += word.count(alphabet)
    word = word.replace(alphabet, '')

answer += len(word)
print(answer)

replace 하면 nljj에서 걸리고 
arr에 있는거 추가해서 하면 dz=ak가 걸림
"""