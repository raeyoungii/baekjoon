import sys

sys.setrecursionlimit(1000000)


def dfs(v, cnt, tmp):
    if c[v] != 0:
        if s[v] == tmp:
            return cnt - c[v]
        return 0
    c[v] = cnt
    s[v] = tmp
    return dfs(adj_lst[v], cnt + 1, tmp)


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    adj_lst = [0]
    # visited 배열
    c = [0] * (n + 1)
    # 재방문 배열
    s = [0] * (n + 1)
    ans = 0
    students = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        adj_lst.append(students[i])
    for i in range(1, n + 1):
        if c[i] == 0:
            ans += dfs(i, 1, i)
    print(n - ans)

# TODO: 모르겠음
