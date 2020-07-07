arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))
for a, b in sorted(arr):
    print(a, b)
