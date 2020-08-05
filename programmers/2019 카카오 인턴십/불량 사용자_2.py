from itertools import product
import re


def solution(user_id, banned_id):
    uid_lst = []
    for b_id in banned_id:  # banned_id에 있는 각 b_id 에서
        b_id = b_id.replace('*', '.')  # 정규 표현식 비교를 위해 *을 .으로 바꿔줌
        uid_tmp = []
        for u_id in user_id:
            # b_id와 u_id를 비교하여 존재하고 b_id와 u_id의 길이가 같으면 (처음이나 끝에 .이 오면 정규 표현식 비교에서 여러 문자가 와도 값을 리턴함)
            if re.match(b_id, u_id) and len(b_id) == len(u_id):
                uid_tmp.append(u_id)  # uid_tmp 배열에 u_id를 추가
        uid_lst.append(uid_tmp)  # 각 b_id와 일치하는 uid_tmp 배열을 uid_lst 배열에 추가
    # u_id 배열의 조합을 구한 뒤 중복된 u_id를 포함하지 않는 i 배열을 정렬한 뒤 튜플로 변환하고 셋으로 변환하여 중복 제거
    answer = set(tuple(sorted(i)) for i in product(*uid_lst) if len(set(i)) == len(banned_id))
    return len(answer)  # 가능한 경우의 수를 리턴


User_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
Banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(User_id, Banned_id))
