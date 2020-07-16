# color[v] = 0, 1, 2
import sys

sys.setrecursionlimit(100000)


def dfs(v, c):
    lst[v] = c
    for nxt in adj_lst[v]:
        if lst[nxt] == 0:
            dfs(nxt, 3 - c)


def bipartite():
    for i in range(1, v + 1):
        for j in adj_lst[i]:
            if lst[i] == lst[j]:
                return False
    return True


k = int(sys.stdin.readline())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    adj_lst = [[] for _ in range(v + 1)]
    lst = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        adj_lst[a].append(b)
        adj_lst[b].append(a)
    for i in range(1, v + 1):
        if lst[i] == 0:
            dfs(i, 1)
    print("YES" if bipartite() else "NO")
