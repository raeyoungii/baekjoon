import sys

S = sys.stdin.readline()
upper_c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_c = "abcdefghijklmnopqrstuvwxyz"
arr = []
for s in S:
    if s.isupper():
        for i in range(len(upper_c)):
            if upper_c[i] == s:
                arr.append(upper_c[i - 13])
    elif s.islower():
        for i in range(len(lower_c)):
            if lower_c[i] == s:
                arr.append(lower_c[i - 13])
    elif s == ' ':
        arr.append(' ')
    else:
        arr.append(s)

print(''.join(arr))
