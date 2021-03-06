import sys

k, n = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(lan)
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in lan:
        cnt += i // mid
    if n <= cnt:
        start = mid + 1
    else:
        end = mid - 1
print(end)
