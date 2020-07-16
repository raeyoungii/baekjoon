def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(N + 1):
        if visit[i] == 0 and matrix[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visit[v] = 0
    while queue:
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, N + 1):
            if visit[i] == 1 and matrix[v][i] == 1:
                queue.append(i)
                visit[i] = 0


N, M, V = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1
dfs(V)
print()
bfs(V)
