import sys


def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] is True:
            for j in range(i + i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] is True] + [n]


N = int(sys.stdin.readline())
PL = prime_list(N)
arr = []
while N != 1:
    for p in PL:
        if N % p == 0:
            arr.append(p)
            N //= p
for p in sorted(arr):
    print(p)

# TODO: 시간복잡도
