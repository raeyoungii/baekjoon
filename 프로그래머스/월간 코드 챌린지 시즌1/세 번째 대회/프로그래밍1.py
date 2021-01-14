def solution(a, b):
    answer = 0
    for i, j in zip(a, b):
        answer += i * j
    return answer


A = [1, 2, 3, 4]
B = [-3, -1, 0, 2]
print(solution(A, B))
