import sys

sys.setrecursionlimit(100000)


def dfs(x, y):
    matrix[x][y] = 0
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]
    for i in range(8):
        n_x = x + dx[i]
        n_y = y + dy[i]
        if 0 <= n_x < h and 0 <= n_y < w:
            if matrix[n_x][n_y] == 1:
                dfs(n_x, n_y)


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    matrix = []
    cnt = 0
    for _ in range(h):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
