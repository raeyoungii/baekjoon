from itertools import permutations


def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] is True:
            for j in range(i + i, n, i):
                sieve[j] = False
    return [str(i) for i in range(2, n) if sieve[i] is True]


def solution(numbers):
    pl = prime_list(10 ** (len(numbers)))
    lst = []
    answer = 0
    for i in range(1, len(numbers) + 1):
        lst += set(map(''.join, permutations(numbers, i)))
    for n in lst:
        if n in pl:
            answer += 1
    return answer


Numbers = "011"
print(solution(Numbers))
