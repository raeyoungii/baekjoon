from collections import Counter


def solution(N, stages):
    cnt = len(stages)
    stages = Counter(stages)
    dic = Counter()
    for i in range(1, N + 1):
        if cnt != 0:
            dic[i] = stages[i] / cnt
            cnt -= stages[i]
        else:
            dic[i] = 0
    answer = [d[0] for d in dic.most_common()]
    return answer


n = 5
Stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n, Stages))
