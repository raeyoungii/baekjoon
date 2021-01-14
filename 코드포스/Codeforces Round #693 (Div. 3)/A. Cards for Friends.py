import sys


def solve():
    w, h, n = map(int, sys.stdin.readline().split())
    paper = 1
    while w % 2 == 0:
        w //= 2
        paper *= 2
    while h % 2 == 0:
        h //= 2
        paper *= 2
    ans = "YES" if paper >= n else "NO"
    print(ans)


cases = int(sys.stdin.readline())
for _ in range(cases):
    solve()
