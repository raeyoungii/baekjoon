def mul(n):
    v = []
    m = int(n ** 0.5)
    for i in range(3, m + 1):
        if n % i == 0:
            v.append(i)
    return v


def solution(brown, yellow):
    total = brown + yellow
    lst = mul(total)
    for i in lst:
        if (i - 2) * (total // i - 2) == yellow:
            return [total // i, i]


Brown = 24
Yellow = 24
print(solution(Brown, Yellow))
