import sys
from collections import deque


def bfs(v):
    vst[v] = True
    while queue:
        now = queue.popleft()
        for nxt in adj_lst[now]:
            if not vst[nxt]:
                vst[nxt] = True
                queue.append(nxt)


n, m = map(int, sys.stdin.readline().split())
adj_lst = [[] for _ in range(n + 1)]
vst = [False] * (n + 1)
queue = deque()
cnt = 0
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj_lst[u].append(v)
    adj_lst[v].append(u)
for i in range(1, n + 1):
    if not vst[i]:
        queue.append(i)
        bfs(i)
        cnt += 1
print(cnt)
