import sys


def solve():
    n = int(sys.stdin.readline())
    a = [0] + list(map(int, sys.stdin.readline().split()))
    b = [0 for _ in range(10 ** 9)]
    for i in range(1, n + 1):
        b[i] += a[i]
        if i + a[i] <= n:
            b[i + a[i]] = max(b[i + a[i]], b[i])
    print(max(b))


cases = int(sys.stdin.readline())
for _ in range(cases):
    solve()
