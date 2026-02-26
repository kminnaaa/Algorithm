num = [int(input()) for _ in range(10)]

mod = []

ans = 0
for n in num:
    if (n % 42) in mod:
        continue
    else:
        mod.append(n % 42)
        ans += 1

print(ans)