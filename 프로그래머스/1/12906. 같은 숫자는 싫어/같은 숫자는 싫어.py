def solution(arr):
    answer = []
    
    for num in arr:
        # 아직 없는 경우
        if num not in answer:
            answer.append(num)
        # 이미 있지만, 연속 아닌 경우
        elif num in answer and answer[-1] != num:
            answer.append(num)
    
    return answer