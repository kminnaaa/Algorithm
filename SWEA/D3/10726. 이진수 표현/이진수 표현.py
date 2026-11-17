TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input().split())

    b = bin(M) # b[2:] -> 순수 이진수
    num = b[2:]
    sample = num[(len(num) - N):]
    # print(num, sample)

    if sample == "1" * N:
        answer = "ON"
    else: answer = "OFF"

    print(f"#{tc} {answer}")