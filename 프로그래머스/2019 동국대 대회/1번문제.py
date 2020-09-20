m = int(input())
tmp = '1'
arr = []
while tmp != '':
    tmp = input()
    arr.append(list(map(int, tmp.split())))
arr.pop()
sorted_x = []
sorted_y = []
lu = []
ld = []
ru = []
rd = []
xcnt1 = xcnt2 = xcnt3 = xcnt4 = ycnt1 = ycnt2 = ycnt3 = ycnt4 = 0

for x, y in arr:
    sorted_x.append(x)
    sorted_y.append(y)
sorted_x.sort()
sorted_y.sort()

for x in sorted_x:
    if x < sorted_x[(m + 1) // 2 - 1] + 1:
        xcnt1 += 1
    else:
        xcnt2 += 1
    if x < sorted_x[(m + 1) // 2 - 1] - 1:
        xcnt3 += 1
    else:
        xcnt4 += 1

for y in sorted_y:
    if y < sorted_y[(m + 1) // 2 - 1] + 1:
        ycnt1 += 1
    else:
        ycnt2 += 1
    if y < sorted_y[(m + 1) // 2 - 1] - 1:
        ycnt3 += 1
    else:
        ycnt4 += 1

if max([xcnt1, xcnt2]) < max([xcnt3, xcnt4]):
    a = sorted_x[(m + 1) // 2 - 1] + 1
else:
    a = sorted_x[(m + 1) // 2 - 1] - 1
if max([ycnt1, ycnt2]) < max([ycnt3, ycnt4]):
    b = sorted_y[(m + 1) // 2 - 1] + 1
else:
    b = sorted_y[(m + 1) // 2 - 1] - 1

for i in arr:
    if i[0] < a and i[1] > b:
        lu.append(i)
    elif i[0] < a and i[1] < b:
        ld.append(i)
    elif i[0] > a and i[1] > b:
        ru.append(i)
    else:
        rd.append(i)

if m != len(arr):
    print("error")
else:
    for i in ru:
        print("({}, {})".format(i[0], i[1]), end=' ')
    print()
    for i in rd:
        print("({}, {})".format(i[0], i[1]), end=' ')
    print()
    for i in lu:
        print("({}, {})".format(i[0], i[1]), end=' ')
    print()
    for i in ld:
        print("({}, {})".format(i[0], i[1]), end=' ')
    print()
