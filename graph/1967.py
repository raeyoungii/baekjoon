import sys

sys.setrecursionlimit(1000000)


def dfs(v):
    vst[v] = True
    for nxt, nxt_d in adj_lst[v]:
        if not vst[nxt]:
            d[nxt] = d[v] + nxt_d
            dfs(nxt)


n = int(sys.stdin.readline())
adj_lst = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    arr = list(map(int, sys.stdin.readline().split()))
    adj_lst[arr[0]].append([arr[1], arr[2]])
    adj_lst[arr[1]].append([arr[0], arr[2]])

vst = [False] * (n + 1)
d = [0] * (n + 1)
dfs(1)

max_d = d.index(max(d))
vst = [False] * (n + 1)
d = [0] * (n + 1)
dfs(max_d)

print(max(d))
