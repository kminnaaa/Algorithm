def solution(clothes):
    answer = 0
    
    dict = {}
    for types in clothes:
        if types[1] in dict:
            dict[types[1]] += 1
        else: dict[types[1]] = 1
    
    # 최소 한개 선택 = 각 key별 value들 +
    combination = 1
    for key in dict:
        combination *= (dict[key] + 1)

    answer = (combination - 1)
    
    return answer