def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solution(w, h):
    ans = w * h - (w + h - gcd(w, h))
    return ans


W = 8
H = 12
print(solution(W, H))
