def solution(n, lost, reserve):
    g = [-1] + [1] * n + [-1]
    for i in lost:
        g[i] -= 1
    for i in reserve:
        g[i] += 1
    for i in range(1, len(g) - 1):
        if g[i] == 0:
            if g[i + 1] == 2:
                g[i] = g[i + 1] = 1
            elif g[i - 1] == 2:
                g[i - 1] = g[i] = 1
    answer = n - g.count(0)
    return answer


N = 5
Lost = [2, 4]
Reserve = [1, 3, 5]
print(solution(N, Lost, Reserve))
