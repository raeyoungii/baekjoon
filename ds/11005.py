N, B = map(int, input().split())
A = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dic = {}
arr = []
for i in range(len(A)):
    dic[i] = A[i]
while N != 0:
    arr.append(dic[N % B])
    N = N // B
print(''.join(reversed(arr)))
