from math import gcd

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            ans += gcd(arr[i], arr[j])
    print(ans)
