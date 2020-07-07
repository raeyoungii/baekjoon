N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())

d = [[0, 0] for _ in range(N)]
d[0][0] = A[0]
for i in range(1, N):
    d[i][0] = max(d[i - 2][0], d[i - 2][1]) + A[i]
    d[i][1] = d[i - 1][0] + A[i]

print(max(d[-1][0], d[-1][1]))
