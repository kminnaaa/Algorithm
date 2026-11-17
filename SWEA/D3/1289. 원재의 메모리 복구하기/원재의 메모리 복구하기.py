T = int(input())

for tc in range(1, T + 1):
    num = input()
    s = "0" * len(num)

    cnt = 0
    for i in range(len(num)):
        if num[i] != s[i]:
            if num[i] == "1":
                s = s[:i] + "1" * (len(num) - i)
                cnt += 1
            else:
                s = s[:i] + "0" * (len(num) - i)
                cnt += 1

        if num == s:
            break

    print(f"#{tc} {cnt}")