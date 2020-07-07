import sys

arr = [list(sys.stdin.readline().split()) for _ in range(int(sys.stdin.readline()))]
for i in sorted(arr, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])):
    print(i[0])
