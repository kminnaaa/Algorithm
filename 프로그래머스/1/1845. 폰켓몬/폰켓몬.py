def solution(nums):
    answer = 0
    
    pocket = {}
    
    for n in nums:
        if n in pocket:
            pocket[n] += 1
        else:
            pocket[n] = 1
    
    # pocket에서.. 2/N개 선택해야 하고, 그중 가짓수가 최대인 경우
    # 2/N개 선택하는 경우 하나씩 다 구하고 그중 가짓수 max 구하기?
    
    # max 구하기
    # 2/N가 pocket의 key 종류보다 작거나 같으면 그냥 2/N개 출력
    # 2/N이 key 종류보다 크면 key가 답
    
    if len(pocket) >= len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(pocket)
    
    return answer