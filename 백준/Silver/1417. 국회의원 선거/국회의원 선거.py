N = int(input())
dasom = int(input())
votes = []

for _ in range(N - 1):
    votes.append(int(input()))

# 다른 모든 사람의 득표수보다 많은 득표수
votes.sort(reverse=True)
count = 0

if not votes:
    print(0)
else:
    while dasom <= votes[0]:
        dasom += 1
        votes[0] -= 1
        count += 1
        votes.sort(reverse=True)
    print(count)