def solution(array, commands):
    answer = []
    tmp = []
    
    # 배열 array의 i번째 ~ j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        tmp = array[(i-1):j]
        tmp.sort()
        answer.append(tmp[k-1])
    
    
    return answer