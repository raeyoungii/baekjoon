import sys


def prime_num(n):
    if n == 1:
        return False
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if n % i == 0:
            return False
    return True


def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] is True:
            for j in range(i + i, n, i):
                sieve[j] = False
    return [i for i in range(2, n // 2 + 1) if sieve[i] is True]


def prime_sum(pl):
    for a in pl:
        if prime_num(N - a):
            return a
    return None


PL = prime_list(1000000)
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    A = prime_sum(PL)
    if A:
        print("{} = {} + {}".format(N, A, N - A))
    else:
        print("Goldbach's conjecture is wrong.")
