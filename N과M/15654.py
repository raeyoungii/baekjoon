import sys


def dfs(idx, n, m):
    if idx == m:
        print(' '.join(map(str, arr)))
        return
    for i, num in enumerate(num_list):
        if vst[i]:
            continue
        vst[i] = True
        arr[idx] = num
        dfs(idx + 1, n, m)
        vst[i] = False


N, M = map(int, sys.stdin.readline().split())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
vst = [False] * (N + 1)
arr = [0] * M
dfs(0, N, M)
