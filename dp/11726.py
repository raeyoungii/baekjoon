N = int(input())
d = [1] + [0] * N
for n in range(1, N + 1):
    d[n] = d[n - 1] + d[n - 2]
print(d[N] % 10007)
