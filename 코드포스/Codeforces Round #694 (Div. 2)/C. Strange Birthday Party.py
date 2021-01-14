import sys


def solve():
    n, m = map(int, sys.stdin.readline().split())
    k = list(reversed(sorted(map(int, sys.stdin.readline().split()))))
    c = list(map(int, sys.stdin.readline().split()))
    idx = 0
    cost = 0
    for i in range(n):
        if idx <= k[i] - 1:
            cost += c[idx]
            idx += 1
        else:
            cost += c[k[i] - 1]
    print(cost)


cases = int(sys.stdin.readline())
for _ in range(cases):
    solve()
