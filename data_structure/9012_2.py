import sys


def is_valid(s):
    cnt = 0
    for x in s:
        if x == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return "NO"
    if cnt == 0:
        return "YES"
    else:
        return "NO"


n = int(sys.stdin.readline())
for i in range(n):
    print(is_valid(sys.stdin.readline().strip()))
