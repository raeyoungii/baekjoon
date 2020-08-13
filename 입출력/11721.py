A = input()

for i in range(len(A)):
    if i % 10 == 0 and i != 0:
        print()
    print(A[i], end='')
