"""
대 : 차 터널 들어가는 순서대로
영 : 나오는 순서대로
반드시 추월했을 차 = 들어갈 때보다 앞쪽으로 온 차
딕셔너리로 > 나올 때 인덱스가 들어갈 때 인덱스보다 작아지면
    > 오답

바로 앞차와 순서 바뀌었는지 확인?
    young에서 숫자가 오름차순 (0,1,2,3) 이어야 함
    + 바로 앞이랑 크기 뒤바뀌면 추월
"""

N = int(input())

dae = {}
young = []
for i in range(N):
    number = input()
    dae[number] = i

for i in range(N):
    number = input()
    young.append(dae[number])

answer = 0
for i in range(N):
    for j in range(i+1, N):
        if young[i] > young[j]:
            answer += 1
            break

print(answer)