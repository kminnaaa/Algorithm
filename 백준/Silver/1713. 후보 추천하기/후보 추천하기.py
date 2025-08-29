"""   
    딕셔너리 - 학생: 추천수, 시간
    1 추천 2 오래된 순 : 람다 쓰려면 요소 어떻게 빼내야 하는지
       > .items() 

오름차순으로 정렬해서 출력
"""

N = int(input())
R = int(input())
students = list(map(int, input().split()))
pictures = {}
time = 0

for s in students:
    time += 1

    # 사진 이미 있는 경우 : 추천수만 증가
    if s in pictures:
        pictures[s][0] += 1
    # 사진 없는 경우
    else:
        # 틀 꽉 찬 경우
        if len(pictures) == N:
            # 추천 적은 순, 시간 작은 순(=오래된 순)
            # x : (번호, [추천, 시간]) x[1][0], x[1][1]
            delete = min(pictures.items(), key=lambda x: (x[1][0], x[1][1]))[0]
            del pictures[delete]
        pictures[s] = [1, time]
        
print(*sorted(pictures))