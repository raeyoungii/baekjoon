N = int(input())
d = [[0 for _ in range(10)] for _ in range(N + 1)]

# d[n][l] += d[n - 1][k] (0 <= k <= l)

for l in range(10):
    d[1][l] = 1

for n in range(2, N + 1):
    for l in range(10):
        for k in range(l + 1):
            d[n][l] += d[n-1][k]

ans = 0
for l in range(10):
    ans += d[N][l]
ans %= 10007

print(ans)
