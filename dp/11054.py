N = int(input())
A = list(map(int, input().split()))

A2 = list(reversed(A))
d = [1 for _ in range(N)]
d2 = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            d[i] = max(d[i], d[j] + 1)
        if A2[j] < A2[i]:
            d2[i] = max(d2[i], d2[j] + 1)
ans = 0
for i in range(N):
    ans = max(ans, d[i] + d2[N - i - 1] - 1)

print(ans)
