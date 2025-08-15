N = int(input())
expr = input().strip()

num = 0          
result = None    
outputs = []     
op = None        

for c in expr:
    if c.isdigit():
        num = num * 10 + int(c)  # 여러 자리 숫자 처리
    else:
        if result is None:
            # 첫 숫자 초기화
            result = num
        else:
            if op == 'S':
                result -= num
            elif op == 'M':
                result *= num
            elif op == 'P':
                result += num
            elif op == 'U':
                if result < 0 and num > 0:
                    result = -((-result) // num)
                elif result > 0 and num < 0:
                    result = -(result // (-num))
                else:
                    result = result // num

        if c == 'C':
            outputs.append(str(result))  # 현재까지 계산된 값 저장

        op = c    # 현재 연산자 저장
        num = 0   # 숫자 초기화

# 출력
if outputs:
    print(' '.join(outputs))
else:
    print("NO OUTPUT")
