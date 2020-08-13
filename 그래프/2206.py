import sys
from collections import deque


def bfs():
    queue.append([0, 0, 0])
    matrix[0][0] = -1
    cnt[0][0][0] = 1
    while queue:
        x, y, flag = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0 and cnt[nx][ny][flag] == 0:  # 이동할 수 있는 곳
                    cnt[nx][ny][flag] = cnt[x][y][flag] + 1
                    queue.append([nx, ny, flag])
                elif matrix[nx][ny] == 1:  # 이동할 수 없는 곳
                    if flag == 0 and cnt[nx][ny][1] == 0:
                        cnt[nx][ny][1] = cnt[x][y][0] + 1
                        queue.append([nx, ny, 1])


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
cnt = [[[0, 0] for _ in range(m)] for _ in range(n)]
queue = deque()
bfs()
a, b = cnt[n - 1][m - 1][0], cnt[n - 1][m - 1][1]
if a != 0 or b != 0:
    if a == 0:
        print(b)
    elif b == 0:
        print(a)
    else:
        print(min(a, b))
else:
    print(-1)
for i in cnt:
    print(*i)