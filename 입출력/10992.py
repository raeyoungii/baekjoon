N = int(input())

print("{0}*".format(' '*(N-1)))
for i in range(N-2):
    print("{0}*{1}*".format(' '*(N-i-2), ' '*(2*(i+1)-1)))
if N != 1:
    print('*'*(2*N-1))
