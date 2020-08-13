N = int(input())
A = list(map(int, input().split()))

d = [0] * N
for i in range(N):
    d[i] = max(A[i], d[i - 1] + A[i])

print(max(d))
