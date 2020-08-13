import sys


def chk(n):
    for i in str(n):
        if i not in btn:
            return False
    return True


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
btn = set(str(i) for i in range(10)) - set(sys.stdin.readline().split())
ans = abs(n - 100)
for i in range(1000001):
    if chk(i) is True:
        ans = min(ans, len(str(i)) + abs(n - i))

print(ans)
