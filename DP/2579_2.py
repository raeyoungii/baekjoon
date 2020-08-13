N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())

d = [0] * N
d[0] = A[0]
for i in range(1, N):
    if N == 2:
        d[1] = d[0] + A[1]
        break
    d[i] = max(d[i - 2] + A[i], d[i - 3] + A[i - 1] + A[i])

print(d[-1])
