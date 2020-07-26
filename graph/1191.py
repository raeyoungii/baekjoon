import sys
from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == '.':
                    matrix[nx][ny] = matrix[x][y]
                    d[nx][ny] = d[x][y] + 1
                    queue.append([nx, ny])


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
t = int(sys.stdin.readline())
for _ in range(t):
    matrix = []
    start = {}
    queue = deque()
    cnt = -1
    ans = ''

    n = int(sys.stdin.readline())

    for _ in range(n):
        matrix.append(list(sys.stdin.readline().strip()))

    d = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'A':
                start['A'] = [i, j]
            if matrix[i][j] == 'B':
                start['B'] = [i, j]
    queue.append(start['A'])
    queue.append(start['B'])
    bfs()

    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and matrix[x][y] != '#' and matrix[nx][ny] != '#':
                    if matrix[x][y] != matrix[nx][ny]:
                        if cnt == -1 or cnt > d[x][y] + d[nx][ny]:
                            cnt = d[x][y] + d[nx][ny]

    print(cnt)
    for i in matrix:
        print(*i)
    for i in d:
        print(*i)
    print()

# TODO: 모름
