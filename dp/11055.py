N = int(input())
A = list(map(int, input().split()))

d = [0 for _ in range(N)]
for i in range(N):
    d[i] = A[i]
    for j in range(i):
        if A[j] < A[i]:
            d[i] = max(d[i], d[j] + A[i])

print(max(d))
