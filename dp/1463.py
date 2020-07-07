#  Bottom-up
N = int(input())
d = [0 for _ in range(N+1)]

for n in range(1, N+1):
    if n == 1:
        d[n] = 0
        continue
    d[n] = d[n-1] + 1
    if n % 3 == 0 and d[n] > d[n//3] + 1:
        d[n] = d[n//3] + 1
    if n % 2 == 0 and d[n] > d[n//2] + 1:
        d[n] = d[n//2] + 1

print(d[N])
