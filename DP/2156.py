N = int(input())
a = [0 for _ in range(10001)]
d = [0 for _ in range(10001)]
for i in range(1, N + 1):
    a[i] = int(input())

# d[i] = d[i-1]
#   if d[i] < d[i-2] + a[i]:
# d[i] = d[i-2] + a[i]
# if d[i] < d[i-3] + a[i-1] + a[i]:
#   d[i] = d[i-3] + a[i-1] + a[i]
#
# or
#
# d[i] = max(d[i-1], d[i-2] + a[i], d[i-3] + a[i-1] + a[i])

d[1] = a[1]
d[2] = a[1] + a[2]
for i in range(3, N + 1):
    d[i] = max(d[i - 1], d[i - 2] + a[i], d[i - 3] + a[i - 1] + a[i])

print(d[N])
