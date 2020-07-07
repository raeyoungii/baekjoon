T = int(input())

for i in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    d = [[0 for _ in range(N + 1)] for _ in range(3)]

    d[0][1] = 0
    d[1][1] = arr[0][0]
    d[2][1] = arr[1][0]
    for n in range(2, N + 1):
        d[0][n] = max(d[0][n - 1], d[1][n - 1], d[2][n - 1])
        d[1][n] = max(d[0][n - 1], d[2][n - 1]) + arr[0][n - 1]
        d[2][n] = max(d[0][n - 1], d[1][n - 1]) + arr[1][n - 1]

    ans = max(d[0][N], d[1][N], d[2][N])
    print(ans)
