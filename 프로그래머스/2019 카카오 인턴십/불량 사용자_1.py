from itertools import product


def solution(user_id, banned_id):
    uid_lst = []
    for b_id in banned_id:
        uid_tmp = []
        bid_idx = []
        for c, i in enumerate(b_id):
            if c == '*':
                bid_idx.append(i)
        for u_id in user_id:
            tmp = list(u_id)
            for i in bid_idx:
                if i < len(tmp):
                    tmp[i] = '*'
            if ''.join(tmp) == b_id:
                uid_tmp.append(u_id)
        uid_lst.append(uid_tmp)
    answer = set(tuple(sorted(i)) for i in product(*uid_lst) if len(set(i)) == len(banned_id))
    return len(answer)


User_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
Banned_id = ["*rodo", "*rodo", "******"]
print(solution(User_id, Banned_id))
