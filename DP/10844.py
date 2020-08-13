N = int(input())
d = [[0 for _ in range(10)] for _ in range(N + 1)]

# d[n][l] = d[n - 1][l - 1] + d[n - 1][l + 1]
for l in range(1, 10):
    d[1][l] = 1
for n in range(2, N + 1):
    for l in range(10):
        if l - 1 >= 0:
            d[n][l] += d[n - 1][l - 1]
        if l + 1 <= 9:
            d[n][l] += d[n - 1][l + 1]

print(sum(d[N]) % 1000000000)
