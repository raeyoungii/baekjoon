N = int(input())

for i in range(N):
    print("{0}{1}".format(' '*i, '*'*(2*(N-i)-1)))

for i in range(N-1):
    print("{0}{1}".format(' '*(N-i-2), '*'*(2*(i+1)+1)))
