import sys
from collections import deque


def dfs(v, lst):
    lst.append(v)
    for nxt in adj_lst[v]:
        if nxt not in lst:
            dfs(nxt, lst)
    return lst


def bfs(v):
    lst = []
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        lst.append(now)
        for nxt in adj_lst[now]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = True
    return lst


N, M, V = map(int, sys.stdin.readline().split())
adj_lst = [[] for _ in range(N + 1)]
queue = deque()
visited = [False for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)
print(*dfs(V, []))
print(*bfs(V))

