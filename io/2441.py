N = int(input())

for i in range(N):
    print("{0}{1}".format(' '*i, '*'*(N-i)))
