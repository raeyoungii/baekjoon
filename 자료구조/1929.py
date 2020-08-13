import sys

min_n, max_n = map(int, sys.stdin.readline().split())
ans = 0


def prime_list(n1, n2):
    # 에라토스테네스의 체 초기화: n2개 요소에 True 설정(소수로 간주)
    sieve = [True] * n2
    # n2의 최대 약수가 sqrt(n) 이하이므로 i = sqrt(n)까지 검사
    m = int(n2 ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] is True:  # i가 소수인 경우
            for j in range(i + i, n2, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False
    # 소수 목록 산출
    return [i for i in range(n1, n2) if sieve[i] is True and i != 1]


for n in prime_list(min_n, max_n + 1):
    print(n)

# TODO: 에라토스테네스의 체
