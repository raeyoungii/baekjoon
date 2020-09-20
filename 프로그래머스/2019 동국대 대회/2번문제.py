from itertools import combinations
from random import shuffle

n, k = map(int, input("N K ? ").split())
s = [i for i in range(-15, 16)]
shuffle(s)
s = s[:n]
print("S={" + ', '.join(map(str, s)) + "}")
print('-' * 30)
hap = []
res = list(combinations(s, 2))
for i in res:
    if sum(i) == k:
        hap.append(i)
if not hap:
    for i in res:
        if sum(i) == k + 1 or sum(i) == k - 1:
            hap.append(i)
if not hap:
    print("Not Found")
else:
    for i in hap:
        print(', '.join(map(str, i)))
