def solution(n):
    answer = 0
    r_n3 = []
    d = 1
    div_3 = n

    while d > 0:
        d, m = divmod(div_3, 3)
        r_n3.append(m)
        div_3 = d

    for n, i in enumerate(r_n3):
        answer += i * (3 ** (len(r_n3) - n - 1))

    return answer


N = 125
print(solution(N))
