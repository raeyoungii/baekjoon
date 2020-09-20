import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(tree)
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in tree:
        if mid < i:
            cnt += i - mid
    if m <= cnt:
        start = mid + 1
    else:
        end = mid - 1
print(end)
