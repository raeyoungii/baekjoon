import sys
from collections import deque


def island_bfs(i_id):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while island_queue:
        x, y = island_queue.popleft()
        matrix[x][y] = i_id
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x < N and 0 <= n_y < N:
                if matrix[n_x][n_y] == 1:
                    matrix[n_x][n_y] = i_id
                    island_queue.append([n_x, n_y])


def bridge_bfs(i_id, b_min):
    cnt = [[0 for _ in range(N)] for _ in range(N)]
    v = [[False for _ in range(N)] for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while bridge_queue:
        x, y = bridge_queue.popleft()
        if b_min < cnt[x][y]:
            return b_min
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] < 0 and matrix[nx][ny] != i_id:
                    return cnt[x][y]
                if matrix[nx][ny] == 0 and v[nx][ny] is False:
                    cnt[nx][ny] = cnt[x][y] + 1
                    v[nx][ny] = True
                    bridge_queue.append([nx, ny])


N = int(sys.stdin.readline())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

island_queue = deque()
island_id = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            island_id -= 1
            island_queue.append([i, j])
            island_bfs(island_id)

bridge_min = 1e5
for n in range(-1, island_id - 1, -1):
    bridge_queue = deque()
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == n:
                bridge_queue.append([i, j])
    bridge_min = bridge_bfs(n, bridge_min)
print(bridge_min)

# TODO: 주석달기
