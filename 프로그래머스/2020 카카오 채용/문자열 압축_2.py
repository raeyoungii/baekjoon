def solution(s):
    length = []

    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1):
        result = ""
        cnt = 1
        tmp = s[:cut]
        for i in range(cut, len(s) + cut, cut):
            if tmp == s[i:i + cut]:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                result += str(cnt) + tmp
                tmp = s[i: i + cut]
                cnt = 1
        length.append(len(result))
    return min(length)


S = "abcabcdede"
print(solution(S))
