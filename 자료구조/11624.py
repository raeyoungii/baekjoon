S = input()
v = []
for i in range(len(S)):
    v.append(''.join(S[i:]))
print('\n'.join(list(sorted(v))))
