import sys
from collections import Counter

n = int(sys.stdin.readline())
n_arr = Counter(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

for i in m_arr:
    print(n_arr[i], end=' ')
