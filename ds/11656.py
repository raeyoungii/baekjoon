from collections import deque

S = deque(input())
S_list = []
while S:
    S_list.append(''.join(S))
    S.popleft()
for i in sorted(S_list):
    print(i)
