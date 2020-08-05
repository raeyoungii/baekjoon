import sys


def binary_search(n):
    start, end = 0, len(n_arr) - 1
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        if n_arr[mid] == n:
            cnt += 1

        elif n_arr[mid] < n:
            start = mid + 1
        else:
            end = mid - 1
    return cnt


n = int(sys.stdin.readline())
n_arr = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

for i in m_arr:
    print(binary_search(i), end=' ')
