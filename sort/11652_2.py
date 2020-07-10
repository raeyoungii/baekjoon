import sys
from collections import Counter

card = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
dic = Counter(sorted(card))
cnt_max = idx = 0
for i in dic:
    if cnt_max < dic[i]:
        cnt_max = dic[i]
        idx = i
print(idx)

# 164ms
