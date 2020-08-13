import re
from copy import deepcopy
from itertools import permutations


def calc(n1, n2, op):
    if op == '*':
        ans = n1 * n2
    elif op == '+':
        ans = n1 + n2
    else:
        ans = n1 - n2
    return ans


def solution(expression):
    n_lst = list(map(int, re.split('[*+-]', expression)))
    o_lst = []
    for o in expression:
        if o in '*+-':
            o_lst.append(o)
    priority = list(permutations(['*', '+', '-']))
    ans_lst = []
    for p in priority:
        tmp_n_lst = deepcopy(n_lst)
        tmp_o_lst = deepcopy(o_lst)
        for i in p:
            j = 0
            for _ in range(len(tmp_o_lst)):
                if tmp_o_lst[j] == i:
                    tmp_n_lst[j] = calc(tmp_n_lst[j], tmp_n_lst[j + 1], i)
                    del tmp_n_lst[j + 1]
                    del tmp_o_lst[j]
                    j -= 1
                j += 1
        ans_lst.append(abs(tmp_n_lst[0]))
    return max(ans_lst)


Expression = "100-200*300-500+20"
print(solution(Expression))
