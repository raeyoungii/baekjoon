import sys


def dfs(v):
    visited[v] = True
    for i in range(N + 1):
        if visited[i] is False and matrix[v][i] == 1:
            dfs(i)


N, M = map(int, sys.stdin.readline().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = 1
    matrix[y][x] = 1
for V in range(1, N + 1):
    if visited[V] is False:
        dfs(V)
        count += 1
print(count)
