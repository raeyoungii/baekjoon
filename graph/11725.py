import sys

sys.setrecursionlimit(1000000)


def dfs(v):
    vst[v] = True
    for nxt in adj_lst[v]:
        if not vst[nxt]:
            parent[nxt] = v
            dfs(nxt)


n = int(sys.stdin.readline())
adj_lst = [[] for _ in range(n + 1)]
vst = [False] * (n + 1)
parent = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

dfs(1)
for i in range(2, n + 1):
    print(parent[i])
