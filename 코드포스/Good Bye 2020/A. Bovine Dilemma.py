import sys
from itertools import combinations


def solve():
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))
    tri_set = set()
    for a, b in combinations(x, 2):
        tri_set.add(b - a)
    print(len(tri_set))


t = int(sys.stdin.readline())
for _ in range(t):
    solve()
