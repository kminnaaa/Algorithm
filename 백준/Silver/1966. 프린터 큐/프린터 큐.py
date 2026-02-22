from collections import deque

T = int(input())

for i in range(T):
    # N: 문서 개수, M: 내 문서가 현재 큐에서 몇 번째에 놓여있는지
    # 왼쪽이 0번째
    # 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.
    N, M = map(int, input().split())
    q = deque(map(int, input().split()))

    cnt = 0
    while q:
        if N == 1:
            print(1)
            break

        # 1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
        front = q.popleft()
        M -= 1

        # 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다.
        if q and max(q) > front:
            q.append(front)
            if M < 0:
                M = len(q) - 1
        # 3. 그렇지 않다면 바로 인쇄를 한다.
        else:
            cnt += 1
            if M < 0:
                print(cnt)
                break
