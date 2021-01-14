from itertools import combinations


def solution(numbers):
    answer = set()
    for i in combinations(numbers, 2):
        answer.add(sum(i))
    return sorted(list(answer))


Numbers = [5, 4, 3]
print(solution(Numbers))
