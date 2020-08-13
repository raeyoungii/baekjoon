import sys

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
n = m = 0
c = []
while n < N and m < M:
    if a[n] < b[m]:
        c.append(a[n])
        n += 1
    else:
        c.append(b[m])
        m += 1
while n < N:
    c.append(a[n])
    n += 1
while m < M:
    c.append(b[m])
    m += 1
print(*c)
