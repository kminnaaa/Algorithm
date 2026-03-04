# T가 S보다 길다
S = input()
T = input()

while len(T) > len(S):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]

if T == S:
    print(1)
else:
    print(0)
"""
문자열의 뒤에 A를 추가한다. --> 문자열의 뒤에서 A를 제거한다
문자열을 뒤집고 뒤에 B를 추가한다. --> 뒤에서 B를 제거하고, 뒤집기
"""