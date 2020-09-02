from math import gcd

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A * B // gcd(A, B))
