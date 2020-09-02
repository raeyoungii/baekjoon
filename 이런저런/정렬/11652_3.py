import sys

N = int(sys.stdin.readline())
dic = {}
for _ in range(N):
    tmp = int(sys.stdin.readline())
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1
dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])

# 168ms
