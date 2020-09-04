import re


def solution(words, queries):
    answer = []
    for q in queries:
        cnt = 0
        q = q.replace('?', '.')
        for w in words:
            if re.match(q, w) and len(q) == len(w):
                cnt += 1
        answer.append(cnt)
    return answer


Words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
Queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(Words, Queries))
