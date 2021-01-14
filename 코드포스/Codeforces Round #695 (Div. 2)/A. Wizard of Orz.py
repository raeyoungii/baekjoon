import sys


def solve():
    n = int(sys.stdin.readline())
    ans = []
    for i in range(n):
        if i == 0:
            ans.append('9')
            continue
        ans.append(str((7 + i) % 10))
    print(''.join(ans))


cases = int(sys.stdin.readline())
for _ in range(cases):
    solve()
