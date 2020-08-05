import sys
from itertools import combinations


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
c_arr = combinations(arr, l)
for i in c_arr:
    if chk(i):
        print(''.join(i))
