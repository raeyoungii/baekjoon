global w, b


def check(x, y, n, arr):
    global w, b
    tmp = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != tmp:
                for k in range(2):
                    for l in range(2):
                        check(x + k * n // 2, y + l * n // 2, n // 2, arr)
                return
    if tmp == 0:
        w += 1
    else:
        b += 1


def solution(arr):
    global w, b
    w, b = 0, 0
    check(0, 0, len(arr), arr)
    answer = [w, b]
    return answer


Arr = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]
print(solution(Arr))
