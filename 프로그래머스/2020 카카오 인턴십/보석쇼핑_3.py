def solution(gems):
    size = len(set(gems))
    dic = {gems[0]: 1}
    answer = []
    min_len = 100001
    start = end = 0
    while start < len(gems) and end < len(gems):
        if len(dic) == size:
            if end - start < min_len:
                min_len = end - start
                answer = [start + 1, end + 1]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] in dic.keys():
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1
    return answer


Gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(Gems))