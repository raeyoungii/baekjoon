import sys
from collections import deque


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x < N and 0 <= n_y < M:
                if matrix[n_x][n_y] == 0:
                    matrix[n_x][n_y] = matrix[x][y] + 1
                    queue.append([n_x, n_y])


def chk():
    ans = 1
    for i in matrix:
        for j in i:
            if j == 0:
                return -1
            if ans < j:
                ans = j
    return ans - 1


M, N = map(int, sys.stdin.readline().split())
matrix = []
queue = deque()
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i, j])
bfs()
print(chk())
