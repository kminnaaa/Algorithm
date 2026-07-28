def solution(phone_book):
    answer = True
    
    # 접두사가 있으면 false 출력
    
    # 그냥 pre in num으로 하면 안되고.. 반드시 pre로 <시작>해야 함
    # phone_book sort 하고
    phone_book.sort()
     
    
    for i in range(0, len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1]:
            flag = phone_book[i+1].split(phone_book[i])
            if flag[0] == "":
                return False

    
    return True
    
