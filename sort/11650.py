import sys

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
for i in sorted(arr, key=lambda x: (x[0], x[1])):
    print(i[0], i[1])
