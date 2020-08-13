T = int(input())
num_list = [0 for _ in range(T + 1)]

for i in range(T):
    num_list[i] = int(input())
    d = [0 for _ in range(num_list[i] + 1)]
    d[0] = d[1] = 1
    if num_list[i] > 1:
        d[2] = 2
        for n in range(3, num_list[i] + 1):
            d[n] = d[n - 1] + d[n - 2] + d[n - 3]
    print(d[num_list[i]])
