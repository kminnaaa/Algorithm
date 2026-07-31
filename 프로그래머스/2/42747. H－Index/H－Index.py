def solution(citations):
    answer = 0
    
    citations.sort()  # [0, 1, 3, 5, 6]
    h_index = [0]
    
    # 논문 n편 중
    # h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index
    n = len(citations)
    
    for i in range(n):
        if citations[i] >= n - i:
            h_index.append(n - i)
    
    answer = max(h_index) if h_index else 0

    return answer