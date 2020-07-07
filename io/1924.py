x, y = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0
wday = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i in range(x-1):
    day += month[i]

day = day + y

print(wday[day % 7])
