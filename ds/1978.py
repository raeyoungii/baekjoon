N = int(input())
arr = list(map(int, input().split()))
cnt = 0


def prime_num(n):
    if n == 1:
        return False
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if n % i == 0:
            return False
    return True


for p in arr:
    cnt += prime_num(p)
print(cnt)
