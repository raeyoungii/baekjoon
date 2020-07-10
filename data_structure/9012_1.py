import sys

T = int(sys.stdin.readline())
for _ in range(T):
    vps = sys.stdin.readline().strip()
    v = []
    f = 0
    for ps in vps:
        if ps == '(':
            v.append(ps)
        else:
            if not v:
                f = 1
                break
            v.pop()
    if not v and f == 0:
        print("YES")
    else:
        print("NO")
