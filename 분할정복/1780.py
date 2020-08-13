import sys


def check(x, y, n):
    global a, b, c
    tmp = matrix[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if matrix[i][j] != tmp:
                for k in range(3):
                    for l in range(3):
                        check(x + k * n // 3, y + l * n // 3, n // 3)
                return
    if tmp == -1:
        a += 1
    elif tmp == 0:
        b += 1
    else:
        c += 1


n = int(sys.stdin.readline())
matrix = [list(map(int, input().split())) for _ in range(n)]
a = b = c = 0
check(0, 0, n)
print(a)
print(b)
print(c)
