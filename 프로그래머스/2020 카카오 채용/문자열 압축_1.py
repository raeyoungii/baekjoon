def solution(s):
    arr = [[] for _ in range(len(s) + 1)]
    arr_len = [[] for _ in range(len(s) + 1)]
    cnt = []
    for i in range(1, len(s) + 1):
        if len(s) % i == 0:
            k = len(s) // i
        else:
            k = len(s) // i + 1
        for j in range(k):
            arr[i].append(s[j * i:(j + 1) * i])

    for i, ar in enumerate(arr):
        idx = 0
        tmp = ''
        for _ in range(len(ar)):
            letter = ar[idx]
            if idx != len(ar) - 1 and ar[idx] == ar[idx + 1]:
                if not arr_len[i]:
                    arr_len[i].append(ar[idx])
                else:
                    if arr_len[i][-1] != ar[idx] or tmp != ar[idx]:
                        arr_len[i].append(ar[idx])
                del ar[idx]
                idx -= 1
            tmp = letter
            idx += 1

    for i in range(len(s) + 1):
        if not arr[i]:
            continue
        if len(s) % i == 0:
            cnt.append(len(arr[i]) * len(arr[i][0]) + len(arr_len[i]))
        else:
            cnt.append((len(arr[i]) - 1) * len(arr[i][0]) + len(arr_len[i]) + len(arr[i][-1]))
    answer = min(cnt)
    return answer


S = "abcabcdede"
print(solution(S))
