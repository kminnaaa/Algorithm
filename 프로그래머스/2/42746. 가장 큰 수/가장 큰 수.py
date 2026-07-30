def solution(numbers):
    answer = ''
    
    str_num = []
    for n in numbers:
        str_num.append(str(n))
    
    str_num.sort(key = lambda x : x*3,reverse=True)
    
    for s in str_num:
        answer += s
    
    if answer[0] == '0':
        return '0'
    else: return answer