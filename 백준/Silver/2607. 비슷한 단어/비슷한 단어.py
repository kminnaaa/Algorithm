"""
단어 구성한 알파벳 종류, 개수 같을 경우 같은 단어

> 비슷 = 한 문자를 더하거나 빼거나 교체해서 같으면
집합? 딕셔너리?
* Counter : 딕셔너리 만들어주는 거

diff_c : 0 > 같은 단어, 1 > 한개 추가/삭제 2 > 교체
"""

from collections import Counter

N = int(input())
first =  input()
count_f = Counter(first)

ans = 0
for _ in range(N-1):
    word = input()
    count_w = Counter(word)

    tmp1 = count_f - count_w    # first에만 있는 알파벳
    tmp2 = count_w - count_f    # 현재 단어에만 있는 알파벳


    diff_c = sum(tmp1.values()) + sum(tmp2.values())
    diff_len = abs(len(first) - len(word))

    
    if diff_c <= 2 and diff_len <= 1:
        ans += 1

print(ans)