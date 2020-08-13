from collections import deque


def solution(board):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    n = len(board)
    cost = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append([0, 0, 0])
    queue.append([0, 0, 1])
    queue.append([0, 0, 2])
    queue.append([0, 0, 3])
    while queue:
        x, y, direction = queue.popleft()  # x축, y축, 방향
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0 and abs(direction - i) != 2:
                    if direction == i:
                        c = cost[x][y][direction] + 100
                    else:
                        c = cost[x][y][direction] + 600
                    if cost[nx][ny][i] > c or cost[nx][ny][i] == 0:
                        cost[nx][ny][i] = c
                        queue.append([nx, ny, i])
    answer = 1000000
    for i in range(4):
        min_cost = cost[n - 1][n - 1][i]
        if min_cost != 0:
            answer = min(answer, min_cost)
    for i in board:
        print(*i)
    return answer


Board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
print(solution(Board))
