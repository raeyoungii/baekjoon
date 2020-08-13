T = int(input())
N = [0] * T
for i in range(T):
    N[i] = int(input())

for n in range(T):
    d = [1, 1, 1, 2, 2] + [0] * (N[n] - 5)
    for i in range(5, N[n]):
        d[i] = d[i - 1] + d[i - 5]
    print(d[N[n] - 1])
