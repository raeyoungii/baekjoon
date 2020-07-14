N, B = map(int, input().split())
NOTATION = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arr = []
while N:
    arr.append(NOTATION[N % B])
    N = N // B
print(''.join(reversed(arr)))
