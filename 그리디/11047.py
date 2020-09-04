import sys

n, k = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
cnt = 0
for i in reversed(arr):
    if k == 0:
        break
    if i <= k:
        a, b = divmod(k, i)
        k = b
        cnt += a
print(cnt)
