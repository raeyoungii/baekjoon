from collections import Counter


def solution(participant, completion):
    ans = Counter(participant) - Counter(completion)
    answer = list(ans)[0]
    return answer

