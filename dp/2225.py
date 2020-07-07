# 합분해
N, K = map(int, input().split())

# d[2][20] = d[1][0] + d[1][1] + d[1][2] + ... + d[1][20]
d = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
d[0][0] = 1
for i in range(1, K + 1):
    for j in range(N + 1):
        for l in range(j + 1):
            d[i][j] += d[i - 1][j - l]
            d[i][j] %= 1000000000

print(d[K][N])
