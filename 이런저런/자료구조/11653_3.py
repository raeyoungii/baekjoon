import sys

num = sys.stdin.readline()
num = int(num)
n = 10000
a = [False, False] + [True] * (n - 1)
primes = []
for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

while True:
    num2 = num
    if num == 1:
        break
    for x in primes:
        if num % x == 0:
            num = num // x
            print(x)
            break
    if num2 == num:
        print(num)
        break
