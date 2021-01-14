import sys


def solve():
    n, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    div = 0
    mod = 0
    max_sum = 0
    for i in a:
        div += i // x
        mod += i % x
        max_sum += i // x
        if i % x != 0:
            max_sum += 1
    if mod % x == 0:
        min_sum = div + mod // x
    else:
        min_sum = div + mod // x + 1
    print(min_sum, max_sum)


cases = int(sys.stdin.readline())
for _ in range(cases):
    solve()
