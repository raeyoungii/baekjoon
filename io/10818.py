N = int(input())
num_list = list(map(int, input().split()))

if N == len(num_list):
    print("{0} {1}".format(min(num_list), max(num_list)))
