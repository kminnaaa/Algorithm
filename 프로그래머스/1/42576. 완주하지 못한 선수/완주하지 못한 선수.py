def solution(participant, completion):
    answer = ''
    # 한명만 완주 못함
    # 이름 중복 가능 > 들어간 인원 중복 가능 > 들어간 인원이랑 나온 인원 비교
    
    dict = {}
    
    for p in participant:
        if p in dict:
            dict[p] += 1
        else:
            dict[p] = 1
    
    for c in completion:
        dict[c] -= 1
    
    for d, v in dict.items():
        if v != 0:
            answer = d
            break
        
    
    return answer