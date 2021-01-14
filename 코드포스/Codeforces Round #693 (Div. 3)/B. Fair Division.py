import sys
from collections import Counter


def solve():
    n = int(sys.stdin.readline())
    a = Counter(map(int, sys.stdin.readline().split()))
    if a[2] % 2 == 0:
        if a[1] % 2 == 0:
            ans = "YES"
        else:
            ans = "NO"
    else:
        if a[1] % 2 == 0 and a[1] >= 2:
            ans = "YES"
        else:
            ans = "NO"
    print(ans)


cases = int(sys.stdin.readline())
for _ in range(cases):
    solve()
