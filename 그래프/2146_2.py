import sys
from collections import deque


def island_bfs(i_id):
    while island_queue:
        x, y = island_queue.popleft()
        matrix[x][y] = i_id
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = i_id
                    island_queue.append([nx, ny])


def bridge_bfs():
    while bridge_queue:
        x, y = bridge_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[x][y]
                    cnt[nx][ny] = cnt[x][y] + 1
                    bridge_queue.append([nx, ny])


def check_cnt():
    min_cnt = -1
    for x in range(N):
        for y in range(N):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if matrix[nx][ny] != matrix[x][y]:
                        if cnt[nx][ny] + cnt[x][y] < min_cnt or min_cnt < 0:
                            min_cnt = cnt[nx][ny] + cnt[x][y]
    return min_cnt


N = int(sys.stdin.readline())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
matrix = []
cnt = [[0 for _ in range(N)] for _ in range(N)]
island_queue = deque()
bridge_queue = deque()
island_id = 0

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            island_id -= 1
            island_queue.append([i, j])
            island_bfs(island_id)

for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            bridge_queue.append([i, j])
bridge_bfs()

print(check_cnt())

# TODO: 주석달기
