n, s = map(int, input().split())
hap = n * (n + 1) // 2 - s
ans = []
for k in range(1, n + 1):
    if ((hap / k) - (k / 2) > 0) and ((hap / k) + (k / 2) < n + 1):
        if k % 2 == 1:
            if hap % k == 0:
                ans.append(k)
        else:
            if (hap / k) - (hap // k) == 0.5:
                ans.append(k)
print(*ans)
