N = int(input())
d = [[0, 0] for _ in range(N + 1)]

d[1][1] = 1
for n in range(2, N + 1):
    d[n][0] = d[n - 1][0] + d[n - 1][1]
    d[n][1] = d[n - 1][0]

ans = d[N][0] + d[N][1]
print(ans)
