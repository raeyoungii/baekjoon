import sys


def solve():
    n, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    min_k = 10 ** 9
    min_a = 0
    for i in range(n):
        k = 1
        tmp = a[i]
        while tmp % x == 0:
            tmp //= x
            k += 1
        if k < min_k:
            min_k = k
            min_a = i

    ans = sum(a) * min_k + sum(a[:min_a])
    print(ans)


cases = int(sys.stdin.readline())
for _ in range(cases):
    solve()
