from collections import defaultdict


def solution(gems):
    start = end = 0
    shop = len(set(gems))
    tmp = defaultdict(int)
    l = 100001
    answer = []
    while True:
        if shop != len(tmp):
            tmp[gems[end]] += 1
            end += 1
        if shop == len(tmp):
            if l > end - start:
                l = end - start
                answer = [start + 1, end]
            if tmp[gems[start]] == 1:
                del tmp[gems[start]]
            else:
                tmp[gems[start]] -= 1
            start += 1
        if end == len(gems) and shop != len(tmp):
            break
    return answer


Gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(Gems))

# sliding window, map
