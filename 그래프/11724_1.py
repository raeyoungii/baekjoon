import sys

sys.setrecursionlimit(10000)


def dfs(v):
    vst[v] = True
    for i in range(1, N + 1):
        if matrix[v][i] == 1:
            if not vst[i]:
                dfs(i)


N, M = map(int, sys.stdin.readline().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
vst = [False] * (N + 1)
count = 0
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = 1
    matrix[y][x] = 1
for i in range(1, N + 1):
    if not vst[i]:
        dfs(i)
        count += 1
print(count)
