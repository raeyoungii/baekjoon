N = int(input())
d = [0 for _ in range(N + 1)]

d[0] = d[1] = 1
for n in range(2, N + 1):
    d[n] = d[n - 1] + d[n - 2]
    d[n] %= 10007

print(d[N])
