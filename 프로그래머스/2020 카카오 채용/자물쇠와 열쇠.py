def attach(x, y, key, lock):
    for i in range(len(key)):
        for j in range(len(key)):
            lock[x + i][y + j] += key[i][j]
    return lock


def detach(x, y, key, lock):
    for i in range(len(key)):
        for j in range(len(key)):
            lock[x + i][y + j] -= key[i][j]
    return lock


def check(n, m, lock):
    for i in range(m):
        for j in range(m):
            if lock[n - 1 + i][n - 1 + j] != 1:
                return False
    return True


def rotate(key):
    return list(zip(*key[::-1]))


def solution(key, lock):
    n = len(key)
    m = len(lock)
    temp_lock = [[0] * (m + 2 * (n - 1)) for _ in range((m + 2 * (n - 1)))]

    # padding
    for i in range(m):
        for j in range(m):
            temp_lock[n - 1 + i][n - 1 + j] = lock[i][j]

    # rotate
    key_90 = rotate(key)
    key_180 = rotate(key_90)
    key_270 = rotate(key_180)

    # matching
    for k in [key, key_90, key_180, key_270]:
        for x in range(m + n - 1):
            for y in range(m + n - 1):
                attach(x, y, k, temp_lock)
                if check(n, m, temp_lock):
                    return True
                detach(x, y, k, temp_lock)
    return False


Key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
Lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(Key, Lock))
