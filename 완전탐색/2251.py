import sys
from collections import deque


def bfs(na, nb, nc):
    queue.append([na, nb, nc])
    while queue:
        na, nb, nc = queue.popleft()
        if [na, nb, nc] in vst:
            continue
        vst.append([na, nb, nc])
        if na == 0:
            ans[nc] = True
        if na + nb > a:
            queue.append([a, na + nb - a, nc])
        else:
            queue.append([na + nb, 0, nc])
        if na + nb > b:
            queue.append([na + nb - b, b, nc])
        else:
            queue.append([0, na + nb, nc])
        if nb + nc > b:
            queue.append([na, b, nb + nc - b])
        else:
            queue.append([na, nb + nc, 0])
        if nb + nc > c:
            queue.append([na, nb + nc - c, c])
        else:
            queue.append([na, 0, nb + nc])
        if nc + na > c:
            queue.append([nc + na - c, nb, c])
        else:
            queue.append([0, nb, nc + na])
        if nc + na > a:
            queue.append([a, nb, nc + na - a])
        else:
            queue.append([nc + na, nb, 0])


a, b, c = map(int, sys.stdin.readline().split())
vst = []
ans = [False] * 201
queue = deque()
bfs(0, 0, c)
for i in range(201):
    if ans[i] is True:
        print(i, end=' ')
