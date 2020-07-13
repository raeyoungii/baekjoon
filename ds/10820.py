import sys

while True:
    S = sys.stdin.readline().rstrip('\n')
    if not S:
        break
    u_cnt = l_cnt = n_cnt = b_cnt = 0
    for s in S:
        if s.isupper():
            u_cnt += 1
        elif s.islower():
            l_cnt += 1
        elif s.isnumeric():
            n_cnt += 1
        elif s == ' ':
            b_cnt += 1
    print(l_cnt, u_cnt, n_cnt, b_cnt)
