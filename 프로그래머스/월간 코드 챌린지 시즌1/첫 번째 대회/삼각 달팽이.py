def solution(n):
    matrix = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1
    for i in range(n):
        for _ in range(n - i):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            matrix[x][y] = num
            num += 1

    idx = 1
    for arr in matrix:
        for i in range(idx):
            answer.append(arr[i])
        idx += 1
    return answer


N = 5
print(solution(N))
