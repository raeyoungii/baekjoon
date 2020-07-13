from collections import deque

N, K = map(int, input().split())
dq = deque([str(i) for i in range(1, N + 1)])
ans = []
while dq:
    dq.rotate(-K + 1)
    ans.append(dq.popleft())
print('<' + ', '.join(ans) + '>')
