import sys

N = int(sys.stdin.readline())
v = []
for _ in range(N):
    cmd = list(sys.stdin.readline().strip().split())
    if cmd[0] == "push":
        v.append(int(cmd[1]))
    elif cmd[0] == "pop":
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
    elif cmd[0] == "top":
        if not v:
            print(-1)
        else:
            print(v[-1])

# `sys.stdin.readline` 은 끝의 개행문자 \n 까지 읽어들이게 됩니다.
# 그렇기 때문에 if cmd == '명령어': 조건식이 전부 False가 되고, else 처리가 없기 때문에 아무런 출력이 없이 종료됩니다.
# 따라서 sys.stdin.readline().strip() 으로 개행문자를 제거해주어야 정상 작동합니다.

# Stack
