N = int(input())

for i in range(N):
    print("{0}{1}".format(' '*(N-i-1), '*'*(i+1)))

for i in range(N-1):
    print("{0}{1}".format(' '*(i+1), '*'*(N-i-1)))
