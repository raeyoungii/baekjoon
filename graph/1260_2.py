import sys


def dfs(v, lst):
    lst.append(v)
    for nxt in adj_lst[v]:
        if nxt not in lst:
            dfs(nxt, lst)
    return lst


def bfs(v):
    lst = []
    q = [v]
    visited[v] = True
    while q:
        now = q.pop(0)
        lst.append(now)
        for nxt in adj_lst[now]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
    return lst


n, m, v = map(int, sys.stdin.readline().split())
adj_lst = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)
print(*dfs(v, []))
print(*bfs(v))
