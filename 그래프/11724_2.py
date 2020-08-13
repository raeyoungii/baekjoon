import sys

sys.setrecursionlimit(100000)


def dfs(v):
    vst[v] = True
    for nxt in adj_lst[v]:
        if not vst[nxt]:
            dfs(nxt)


n, m = map(int, sys.stdin.readline().split())
adj_lst = [[] for _ in range(n + 1)]
vst = [False] * (n + 1)
cnt = 0
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj_lst[u].append(v)
    adj_lst[v].append(u)
for i in range(1, n + 1):
    if not vst[i]:
        dfs(i)
        cnt += 1
print(cnt)
