# 백준 15903 - 카드 합체 놀이

"""
자연수가 쓰여진 카드 n장
처음에 i번 카드엔 ai가 쓰여있다

x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.
합체를 총 m번 하면 놀이가 끝난다
m번의 합체를 모두 끝낸 뒤, n장의 카드에 쓰여있는 수를 모두 더한 값이 이 놀이의 점수가 된다. 이 점수를 가장 작게 만드는 것이 놀이의 목표이다.
최소 점수는?
"""

N, M = map(int, input().split())
cards = list(map(int, input().split()))

for _ in range(M):
    cards.sort()  # 가장 작은 두 장 찾기
    s = cards[0] + cards[1]
    cards[0] = s
    cards[1] = s

print(sum(cards))