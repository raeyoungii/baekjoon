import sys


def solve():
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))
    n_set = set()
    for item in x:
        if item not in n_set:
            n_set.add(item)
        else:
            n_set.add(item + 1)
    print(len(n_set))


t = int(sys.stdin.readline())
for _ in range(t):
    solve()
