import sys

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))
cnt_arr = set(m_arr) - set(n_arr)
for i in m_arr:
    if i in cnt_arr:
        print(0, end=' ')
    else:
        print(1, end=' ')
