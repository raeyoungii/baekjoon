import sys


def dfs(v):
    vst[v] = True
    for nxt, nxt_d in adj_lst[v]:
        if not vst[nxt]:
            d[nxt] = d[v] + nxt_d
            dfs(nxt)


v = int(sys.stdin.readline())
adj_lst = [[] for _ in range(v + 1)]
for _ in range(v):
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(arr) - 1, 2):
        adj_lst[arr[0]].append([arr[i], arr[i + 1]])

vst = [False] * (v + 1)
d = [0] * (v + 1)
dfs(1)

max_v = d.index(max(d))
vst = [False] * (v + 1)
d = [0] * (v + 1)
dfs(max_v)

print(max(d))
