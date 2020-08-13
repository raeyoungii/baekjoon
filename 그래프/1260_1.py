import sys
from collections import deque


def dfs(v):
    vst[v] = True
    print(v, end=' ')
    for i in range(1, n + 1):
        if matrix[v][i] == 1:
            if not vst[i]:
                dfs(i)


def bfs(v):
    queue.append(v)
    vst[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if matrix[v][i] == 1:
                if not vst[i]:
                    queue.append(i)
                    vst[i] = True


n, m, v = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

vst = [False] * (n + 1)
dfs(v)
print()

vst = [False] * (n + 1)
queue = deque()
bfs(v)
