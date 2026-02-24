N = int(input())
words = [input() for _ in range(N)]

words.sort()

ans = N
for i in range(N-1):
    target_length = len(words[i])
    if words[i] == words[i+1][:target_length]:
        ans -= 1

print(ans)