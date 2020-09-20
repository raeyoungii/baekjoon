import sys


def dfs(idx, n, m):
    if idx == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n + 1):
        vst[i] = True
        arr[idx] = i
        dfs(idx + 1, n, m)
        vst[i] = False


N, M = map(int, sys.stdin.readline().split())
vst = [False] * (N + 1)
arr = [0] * M
dfs(0, N, M)
