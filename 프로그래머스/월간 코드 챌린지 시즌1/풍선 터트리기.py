def solution(a):
    answer = 2
    left, right = a[0], a[-1]

    if 0 <= len(a) <= 2:
        return len(a)

    for i in range(1, len(a) - 1):
        if left > a[i]:
            answer += 1
            left = a[i]
        if right > a[-1 - i]:
            answer += 1
            right = a[-1 - i]

    if left == right:
        answer -= 1

    return answer


A = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
print(solution(A))
