import sys


def check(x, y, n):
    global w, b
    tmp = matrix[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if matrix[i][j] != tmp:
                for k in range(2):
                    for l in range(2):
                        check(x + k * n // 2, y + l * n // 2, n // 2)
                return
    if tmp == 0:
        w += 1
    else:
        b += 1


n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
w = b = 0
check(0, 0, n)
print(w)
print(b)
