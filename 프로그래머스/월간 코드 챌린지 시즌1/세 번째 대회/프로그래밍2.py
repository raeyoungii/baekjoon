from copy import deepcopy


def solution(s):
    tmp = s
    arr = ""
    cnt = 0
    zero = 0

    while True:
        cnt += 1
        for i in tmp:
            if i == '1':
                arr += i
            else:
                zero += 1

        arr = format(len(arr), 'b')
        if arr == '1':
            break

        tmp = deepcopy(arr)
        arr = ""

    answer = [cnt, zero]
    return answer


S = "110010101001"
print(solution(S))
