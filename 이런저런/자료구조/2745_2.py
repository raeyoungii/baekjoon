N, B = input().split()
B = int(B)
ans, cnt = 0, 0
for c in N[::-1]:
    tmp = int(c) if c.isdigit() else ord(c) - 55
    ans += tmp * (B ** cnt)
    cnt += 1
print(ans)
