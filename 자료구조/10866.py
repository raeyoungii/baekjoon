import sys
import collections

N = int(sys.stdin.readline())
v = collections.deque()
for _ in range(N):
    cmd = list(sys.stdin.readline().strip().split())
    if cmd[0] == "push_front":
        v.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        v.append(cmd[1])
    elif cmd[0] == "pop_front":
        if not v:
            print(-1)
        else:
            print(v.popleft())
    elif cmd[0] == "pop_back":
        if not v:
            print(-1)
        else:
            print(v.pop())
    elif cmd[0] == "size":
        print(len(v))
    elif cmd[0] == "empty":
        if not v:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if not v:
            print(-1)
        else:
            print(v[0])
    elif cmd[0] == "back":
        if not v:
            print(-1)
        else:
            print(v[-1])
