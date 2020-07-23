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
                if adj_lst[n_x][n_y] == 1:
                    adj_lst[n_x][n_y] = adj_lst[x][y] + 1
                    queue.append([n_x, n_y])


N, M = map(int, sys.stdin.readline().split())
adj_lst = []
queue = deque([[0, 0]])
for _ in range(N):
    adj_lst.append(list(map(int, list(sys.stdin.readline().strip()))))
bfs()
print(adj_lst[N - 1][M - 1])
