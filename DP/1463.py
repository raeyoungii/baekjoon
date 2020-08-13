#  Bottom-up
N = int(input())
d = [0] * (N + 1)
for n in range(2, N + 1):
    d[n] = d[n - 1] + 1
    if n % 3 == 0 and d[n] > d[n // 3] + 1:
        d[n] = d[n // 3] + 1
    if n % 2 == 0 and d[n] > d[n // 2] + 1:
        d[n] = d[n // 2] + 1
print(d[N])
