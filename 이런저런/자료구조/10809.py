import sys

S = sys.stdin.readline()
d = {}
al = "abcdefghijklmnopqrstuvwxyz"
for a in al:
    d[a] = -1
for s in S:
    for i in d.keys():
        if s == i:
            d[i] = S.index(s)
ans = list(d.values())
for i in ans:
    print(i, end=' ')
