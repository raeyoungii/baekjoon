import sys


def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = [0 for _ in range(n)]
    base = 0
    for i in range(1, n - 1):
        if a[i] < a[i + 1] and a[i] < a[i - 1]:
            b[i] = 1
        if a[i] > a[i + 1] and a[i] > a[i - 1]:
            b[i] = 1
        base += b[i]
    ans = base
    for i in range(1, n - 1):
        val = a[i]
        for j in range(-1, 2, 2):
            tmp = base
            a[i] = a[i + j]
            for k in range(i - 1, i + 2):
                if k == 0:
                    continue
                if k == n - 1:
                    continue
                tmp -= b[k]
                if a[k] < a[k + 1] and a[k] < a[k - 1]:
                    tmp += 1
                if a[k] > a[k + 1] and a[k] > a[k - 1]:
                    tmp += 1
            if tmp < ans:
                ans = tmp
        a[i] = val
    print(ans)


cases = int(sys.stdin.readline())
for _ in range(cases):
    solve()
