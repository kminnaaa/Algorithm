def solution(N, stages):
    answer = []

    size = len(stages)
    dict = {}
    for i in range(1, N + 1):
        if (stages.count(i) == 0):
            dict[i] = 0
            continue

        dict[i] = stages.count(i) / size
        size -= stages.count(i)

    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    for i in dict:
        answer.append(i[0])

    return answer