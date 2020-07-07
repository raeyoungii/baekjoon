N = int(input())

for i in range(N):
    print("{0}{1}".format(' '*(N-i-1), '*'*(2*i+1)))
