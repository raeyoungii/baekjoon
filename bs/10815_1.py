import sys


def binary_search(n):
    start, end = 0, len(n_arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if n_arr[mid] == n:
            return True
        elif n_arr[mid] < n:
            start = mid + 1
        else:
            end = mid - 1
    return False


n = int(sys.stdin.readline())
n_arr = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

for i in m_arr:
    if binary_search(i):
        print(1, end=' ')
    else:
        print(0, end=' ')
