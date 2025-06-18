"""
앞에서부터 정해진 길이만큼
 : 절반 이하 길이로만 슬라이스
 하나씩 ~ 절반 까지 해보기?
 ????
"""

def solution(s):
    answer = len(s)
    
    for i in range(1, (len(s)//2)+1):
        string = ''
        temp = s[0:i]   # i까지 슬라이스
        count = 1
        for j in range(i, len(s), i):
            if temp == s[j:j+i]:
                count += 1
            else:
                if count >= 2:
                    string += str(count) + temp
                else:
                    string += temp
                temp = s[j:j+i]
                count = 1
        if count >= 2:
            string += str(count) + temp
        else:
            string += temp
        answer = min(answer, len(string))        
    
    return answer