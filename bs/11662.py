import sys


def distance(x1, y1, x2, y2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    return d


Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, sys.stdin.readline().split())
ABx = (Bx - Ax) / 1000000
ABy = (By - Ay) / 1000000
CDx = (Dx - Cx) / 1000000
CDy = (Dy - Cy) / 1000000
min_d = -1
for i in range(1000001):
    d = distance(Ax + ABx * i, Ay + ABy * i, Cx + CDx * i, Cy + CDy * i)
    if d < min_d or min_d < 0:
        min_d = d
print(min_d)

# 삼분탐색
