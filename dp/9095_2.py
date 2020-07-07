T = int(input())
d = [0 for _ in range(11)]

d[0] = 1
for n in range(11):
    if n - 1 >= 0:
        d[n] += d[n - 1]
    if n - 2 >= 0:
        d[n] += d[n - 2]
    if n - 3 >= 0:
        d[n] += d[n - 3]

for _ in range(T):
    N = int(input())
    print(d[N])
