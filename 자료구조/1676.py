import sys
N = int(sys.stdin.readline())
ans, cnt = 1, 0
for i in range(2, N + 1):
    ans *= i
while True:
    if ans % 10 != 0:
        break
    cnt += 1
    ans //= 10
print(cnt)
