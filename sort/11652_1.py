import sys

v = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
v.sort()
cnt = cnt_max = 1
ans = v[0]
for i in range(1, len(v)):
    if v[i] != v[i - 1]:
        cnt = 1
    else:
        cnt += 1
        if cnt_max < cnt:
            cnt_max = cnt
            ans = v[i]
print(ans)

# 180ms
