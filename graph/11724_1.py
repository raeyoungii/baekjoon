import sys


def dfs(v):
    visit[v] = 1
    for i in range(N + 1):
        if visit[i] == 0 and matrix[v][i] == 1:
            dfs(i)


N, M = map(int, sys.stdin.readline().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
count = 0
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = 1
    matrix[y][x] = 1
for V in range(1, N + 1):
    if visit[V] == 0:
        dfs(V)
        count += 1
print(count)
