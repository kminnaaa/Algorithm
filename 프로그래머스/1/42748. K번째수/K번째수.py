def solution(array, commands):
    answer = []
    
    for ijk in commands:
        tmp = []
        tmp = array[ijk[0] - 1:ijk[1]]
        tmp.sort()
        answer.append(tmp[ijk[2] - 1])
    
    return answer