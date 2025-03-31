# 백준 10162

T = int(input(""))

button_types = [300, 60, 10]
count = 0

button_count = []

if T % 10 != 0:
    print(-1)
else:
    for button in button_types:
        count = T // button
        T %= button
        button_count.append(count)
    print(button_count[0], button_count[1], button_count[2])