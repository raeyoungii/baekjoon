import sys
from collections import deque


def island_bfs(i_id):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while island_queue:
        x, y = island_queue.popleft()
        adj_lst[x][y] = i_id
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x < N and 0 <= n_y < N:
                if adj_lst[n_x][n_y] == 1:
                    adj_lst[n_x][n_y] = i_id
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
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x < N and 0 <= n_y < N:
                if adj_lst[n_x][n_y] < 0 and adj_lst[n_x][n_y] != i_id:
                    return cnt[x][y]
                if adj_lst[n_x][n_y] == 0 and v[n_x][n_y] is False:
                    cnt[n_x][n_y] = cnt[x][y] + 1
                    v[n_x][n_y] = True
                    bridge_queue.append([n_x, n_y])


N = int(sys.stdin.readline())

adj_lst = []
for _ in range(N):
    adj_lst.append(list(map(int, sys.stdin.readline().split())))

island_queue = deque()
island_id = 0
for i in range(N):
    for j in range(N):
        if adj_lst[i][j] == 1:
            island_id -= 1
            island_queue.append([i, j])
            island_bfs(island_id)

bridge_min = 1e5
for n in range(-1, island_id - 1, -1):
    bridge_queue = deque()
    for i in range(N):
        for j in range(N):
            if adj_lst[i][j] == n:
                bridge_queue.append([i, j])
    bridge_min = bridge_bfs(n, bridge_min)
print(bridge_min)

# TODO: 주석달기
