import sys

arr = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
for i in sorted(arr):
    print(i)
