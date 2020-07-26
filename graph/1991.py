import sys

sys.setrecursionlimit(100000)


def preorder(c):
    print(c, end='')
    if adj_lst[ord(c) - 65][0] != '.':
        preorder(adj_lst[ord(c) - 65][0])
    if adj_lst[ord(c) - 65][1] != '.':
        preorder(adj_lst[ord(c) - 65][1])


def inorder(c):
    if adj_lst[ord(c) - 65][0] != '.':
        inorder(adj_lst[ord(c) - 65][0])
    print(c, end='')
    if adj_lst[ord(c) - 65][1] != '.':
        inorder(adj_lst[ord(c) - 65][1])


def postorder(c):
    if adj_lst[ord(c) - 65][0] != '.':
        postorder(adj_lst[ord(c) - 65][0])
    if adj_lst[ord(c) - 65][1] != '.':
        postorder(adj_lst[ord(c) - 65][1])
    print(c, end='')


N = int(sys.stdin.readline())
adj_lst = [[0] * 2 for _ in range(26)]
for _ in range(N):
    c, l, r = sys.stdin.readline().split()
    adj_lst[ord(c) - 65][0] = l
    adj_lst[ord(c) - 65][1] = r

preorder('A')
print()
inorder('A')
print()
postorder('A')
