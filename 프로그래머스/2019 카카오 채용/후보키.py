from itertools import combinations


def solution(relation):
    col_len = len(relation[0])
    row_len = len(relation)

    arr = []
    for i in range(1, col_len + 1):
        arr.extend(set(k) for k in combinations([j for j in range(col_len)], i))

    unique_set = []
    for c in arr:
        temp_set = set()
        for i in range(row_len):
            tmp = ''
            for j in c:
                tmp += relation[i][j]
            temp_set.add(tmp)
        if len(temp_set) == row_len:
            unique_set.append(c)

    min_set = set()
    for i, j in combinations(unique_set, 2):
        if i.issubset(j):
            min_set.add(unique_set.index(j))

    answer = len(unique_set) - len(min_set)
    return answer


Relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
print(solution(Relation))

# TODO: 다시풀기
