import sys

n, c = map(int, sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline()) for _ in range(n)])
start, end = 1, house[-1] - house[0]
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    ih = house[0]
    for i in range(1, n):
        if mid <= house[i] - ih:
            cnt += 1
            ih = house[i]
    if c <= cnt:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)
