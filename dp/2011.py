N = [0] + list(map(int, input()))
d = [1] + [0 for _ in range(len(N) - 1)]
for i in range(1, len(N)):
    if N[i] != 0:
        d[i] += d[i - 1]
    if i == 1:
        continue
    x = N[i - 1] * 10 + N[i]
    if (10 <= x) and (x <= 26):
        d[i] += d[i - 2]
print(d[len(N) - 1] % 1000000)
