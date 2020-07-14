import string

N, B = map(int, input().split())
NOTATION = string.digits + string.ascii_uppercase


def num_sys(num, base):
    q, r = divmod(num, base)
    n = NOTATION[r]
    return num_sys(q, base) + n if q else n


print(num_sys(N, B))
