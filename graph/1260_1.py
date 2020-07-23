def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in range(N + 1):
        if matrix[v][i] == 1 and visited[i] is False:
            dfs(i)


def bfs(v):
    queue = [v]
    visited[v] = True
    while queue:
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, N + 1):
            if matrix[v][i] == 1 and visited is False:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1
dfs(V)
print()
visited = [False for _ in range(N + 1)]
bfs(V)
