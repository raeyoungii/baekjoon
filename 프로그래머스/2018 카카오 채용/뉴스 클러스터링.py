from collections import Counter


def solution(str1, str2):
    str1_arr = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    str2_arr = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    if not str1_arr and not str2_arr:
        return 65536

    str1_cnt = Counter(str1_arr)
    str2_cnt = Counter(str2_arr)

    str_intersection = set(str1_arr) & set(str2_arr)
    str_union = set(str1_arr) | set(str2_arr)

    intersection = sum(min(str1_cnt[i], str2_cnt[i])for i in str_intersection)
    union = sum(max(str1_cnt[i], str2_cnt[i]) for i in str_union)

    jaccard = int(intersection / union * 65536)

    return jaccard


Str1 = 'FRANCE'
Str2 = 'french'
print(solution(Str1, Str2))
