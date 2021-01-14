from collections import Counter


def solution(a):
    answer = 0
    max_num = Counter(a).most_common(1)[0][0]
    i = 0

    for _ in range(len(a)):
        if i > len(a) - 2:
            break
        if a[i] != max_num and a[i + 1] != max_num:
            i += 1
            continue
        if a[i] == max_num and a[i + 1] == max_num:
            i += 1
            continue
        answer += 2
        i += 2
    return answer


A = [2, 2, 3, 1, 3]
print(solution(A))
