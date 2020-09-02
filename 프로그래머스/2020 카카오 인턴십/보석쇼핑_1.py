from collections import deque


def solution(gems):
    start = end = 0
    shop = set(gems)
    tmp = deque()
    l = 100001
    answer = []
    while True:
        if shop != set(tmp):
            tmp.append(gems[end])
            end += 1
        if shop == set(tmp):
            if l > end - start:
                l = end - start
                answer = [start + 1, end]
            tmp.popleft()
            start += 1
        if end == len(gems) and shop != set(tmp):
            break
    return answer


Gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(Gems))

# 시간초과
