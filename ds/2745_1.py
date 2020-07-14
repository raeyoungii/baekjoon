N, B = input().split()
B = int(B)
A = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dic = {}
arr = []
for i in range(len(A)):
    dic[A[i]] = i
for i in range(len(N)):
    arr.append(dic[N[i]] * B ** (len(N) - i - 1))
print(sum(arr))
