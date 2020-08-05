import sys


def dfs(pwd, idx):
    if len(pwd) == l:
        if chk(pwd):
            print(''.join(pwd))
            return
    if idx < len(arr):
        dfs(pwd + list(arr[idx]), idx + 1)
        dfs(pwd, idx + 1)


def chk(pwd):
    mo = 0
    for i in pwd:
        if i in vowel:
            mo += 1
    if mo >= 1 and l - mo >= 2:
        return True
    else:
        return False


vowel = 'aeiou'
l, c = map(int, sys.stdin.readline().split())
arr = sorted(list(sys.stdin.readline().split()))
dfs([], 0)
