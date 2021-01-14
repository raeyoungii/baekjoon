from itertools import combinations


def solution(s):
    answer = 0
    for i in range(len(s)):
        tmp = 0
        for j in range(i, len(s)):
            if s[i] != s[j]:
                tmp = j - i
                answer += tmp
            else:
                answer += tmp
    return answer


S = "baby"
print(solution(S))
