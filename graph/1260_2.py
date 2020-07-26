import sys
from collections import deque


def dfs(v, lst):
    lst.append(v)
    vst1[v] = True
    for nxt in adj_lst[v]:
        if not vst1[nxt]:
            dfs(nxt, lst)
    return lst


def bfs(v):
    lst = []
    queue.append(v)
    vst2[v] = True
    while queue:
        now = queue.popleft()
        lst.append(now)
        for nxt in adj_lst[now]:
            if not vst2[nxt]:
                vst2[nxt] = True
                queue.append(nxt)
    return lst


N, M, V = map(int, sys.stdin.readline().split())
adj_lst = [[] for _ in range(N + 1)]
queue = deque()
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)
for i in range(1, N + 1):
    adj_lst[i].sort()

vst1 = [False] * (N + 1)
print(*dfs(V, []))
vst2 = [False] * (N + 1)
print(*bfs(V))
