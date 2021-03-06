import sys

sys.setrecursionlimit(1000000)


def dfs(x, y, cnt):
    matrix[x][y] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        if 0 <= n_x < N and 0 <= n_y < N:
            if matrix[n_x][n_y] == 1:
                cnt = dfs(n_x, n_y, cnt + 1)
    return cnt


N = int(sys.stdin.readline())
matrix = []
lst = []
for _ in range(N):
    matrix.append(list(map(int, list(sys.stdin.readline().strip()))))
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            lst.append(dfs(i, j, 1))
print(len(lst))
for i in sorted(lst):
    print(i)
