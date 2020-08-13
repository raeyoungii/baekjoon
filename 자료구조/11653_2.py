import sys

v = int(sys.stdin.readline())
i = 2
while v != 1:
    if v % i == 0:
        v = v / i
        print(i)
    else:
        i += 1
