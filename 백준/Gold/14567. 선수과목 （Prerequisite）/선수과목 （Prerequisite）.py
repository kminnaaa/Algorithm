from collections import deque

# 선수과목 없는거 무조건 1학기, 선수과목 있으면 선수과목학기 + 1학기 (여러개일 경우 가장 늦은 선수과목 기준)
N, M = map(int, input().split())
# 선수과목 리스트(seq), 선수과목 개수 리스트(pre_nums), 몇 학기에 듣게 되는지 저장하는 리스트(ans)
seq = [[] for _ in range(N+1)]
pre_nums = [0 for _ in range(N+1)]
ans = [0 for _ in range(N+1)]

for i in range(M):
    # 항상 1 <= A < B <= N
    A, B = map(int, input().split())

    seq[A].append(B)
    pre_nums[B] += 1

# 선수과목 없는거 = 1학기에 듣는거 찾기
q = deque()
for i in range(1, N + 1):
    if pre_nums[i] == 0:
        q.append(i)
        ans[i] = 1

while q:
    tmp = q.popleft()
    for i in seq[tmp]:
        pre_nums[i] -= 1
        ans[i] = max(ans[tmp] + 1, ans[i])
        if pre_nums[i] == 0:
            q.append(i)
    
print(*ans[1:])