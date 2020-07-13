import sys
l_stk = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline())
r_stk = []
for _ in range(M):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'P':
        l_stk.append(cmd[1])
    if cmd[0] == 'L':
        if l_stk:
            r_stk.append(l_stk.pop())
    if cmd[0] == 'D':
        if r_stk:
            l_stk.append(r_stk.pop())
    if cmd[0] == 'B':
        if l_stk:
            l_stk.pop()
print(''.join(l_stk) + ''.join(reversed(r_stk)))
