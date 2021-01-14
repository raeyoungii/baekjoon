import sys

sys.setrecursionlimit(1000000)


def reset_arr(n):
    vst = [False] * (n + 1)
    d = [0] * (n + 1)
    return vst, d


def dfs(v, vst, d, adj_lst):
    vst[v] = True
    for nxt in adj_lst[v]:
        if not vst[nxt]:
            d[nxt] = d[v] + 1
            dfs(nxt, vst, d, adj_lst)


def solution(n, edges):
    adj_lst = [[] for _ in range(n + 1)]
    for i, j in edges:
        adj_lst[i].append(j)
        adj_lst[j].append(i)

    vst, d = reset_arr(n)
    dfs(1, vst, d, adj_lst)  # v1 = 1
    v2 = d.index(max(d))

    vst, d = reset_arr(n)
    dfs(v2, vst, d, adj_lst)
    if d.count(max(d)) > 1:
        return max(d)
    v3 = d.index(max(d))

    vst, d = reset_arr(n)
    dfs(v3, vst, d, adj_lst)
    # v4 = d.index(max(d))
    if d.count(max(d)) > 1:
        answer = max(d)
    else:
        answer = max(d) - 1

    return answer


N = 5
Edges = [[1, 5], [2, 5], [3, 5], [4, 5]]
print(solution(N, Edges))
