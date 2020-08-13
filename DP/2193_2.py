N = int(input())
d = [0 for _ in range(91)]

d[1] = d[2] = 1
for n in range(3, N + 1):
    d[n] = d[n - 1] + d[n - 2]

ans = d[N]
print(ans)
