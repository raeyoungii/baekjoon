import sys


def dfs(v):
    c[v] = True
    for nxt in adj_lst[v]:
        if not c[nxt]:
            dfs(nxt)


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    adj_lst = [[] for _ in range(N + 1)]
    c = [False] * (N + 1)
    cnt = 0
    for i in range(N):
        adj_lst[i + 1].append(arr[i])
        adj_lst[arr[i]].append(i + 1)
    for v in range(1, N + 1):
        if not c[v]:
            dfs(v)
            cnt += 1
    print(cnt)
