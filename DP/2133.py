N = int(input())

d = [0] * (N + 1)
d[0] = 1
for i in range(2, N + 1, 2):
    d[i] = 3 * d[i - 2]
    for j in range(4, i + 1, 2):
        d[i] += 2 * d[i - j]

print(d[N])
