import sys


def solve():
    in_ = list(sys.stdin.readline().strip())
    n = len(in_)
    used = [False for _ in range(n)]
    ans = 0
    for i in range(1, n):
        use_need = False
        if in_[i] == in_[i - 1] and not used[i - 1]:
            use_need = True
        if i > 2 and in_[i] == in_[i - 2] and not used[i - 2]:
            use_need = True
        used[i] = use_need
        ans += used[i]
    print(ans)


cases = int(sys.stdin.readline())
for _ in range(cases):
    solve()

# 7
# babba
# abaac
# codeforces
# zeroorez
# abcdcba
# bbbbbbb
# a
