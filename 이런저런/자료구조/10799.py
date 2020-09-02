import sys

vps = sys.stdin.readline().strip()
v = []
ans = 0
for (i, c) in enumerate(vps):
    if c == '(':
        v.append(i)
    else:
        if v[-1] + 1 == i:
            v.pop()
            ans += len(v)
        else:
            v.pop()
            ans += 1

print(ans)
