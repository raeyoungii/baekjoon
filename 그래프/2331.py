import sys

sys.setrecursionlimit(100000)


def chk(v, cnt):
    if lst[v] != 0:
        return lst[v] - 1
    lst[v] = cnt
    return chk(nxt(v), cnt + 1)


def nxt(v):
    str_v = str(v)
    tmp = 0
    for i in range(len(str_v)):
        tmp += int(str_v[i]) ** P
    return tmp


A, P = map(int, sys.stdin.readline().split())
lst = [0] * 1000000
print(chk(A, 1))
