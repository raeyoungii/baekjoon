import sys
from collections import deque


def dfs(v):
    lst.append(v)
    vst[v] = True
    for nxt in adj_lst[v]:
        if not vst[nxt]:
            dfs(nxt)


def bfs(v):
    queue.append(v)
    vst[v] = True
    while queue:
        now = queue.popleft()
        lst.append(now)
        for nxt in adj_lst[now]:
            if not vst[nxt]:
                queue.append(nxt)
                vst[nxt] = True


n, m, v = map(int, sys.stdin.readline().split())
adj_lst = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)
for i in range(n + 1):
    adj_lst[i].sort()

lst = []
vst = [False] * (n + 1)
dfs(v)
print(*lst)

lst = []
vst = [False] * (n + 1)
queue = deque()
bfs(v)
print(*lst)
