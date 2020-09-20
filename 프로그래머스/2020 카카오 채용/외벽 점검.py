from itertools import permutations


def solution(n, weak, dist):
    answer = []
    weak_extend = weak + [w + n for w in weak]
    for i, start in enumerate(weak):
        for friends in permutations(dist):
            cnt = 1
            pos = start
            for friend in friends:
                pos += friend
                # 끝 포인트를 도달 못했을때
                if pos < weak_extend[i + len(weak) - 1]:
                    cnt += 1
                    # 현재 위치보다 멀리 있는 취약지점 중 가장 가까운 위치로
                    pos = [w for w in weak_extend[i + 1:i + len(weak)] if w > pos][0]
                # 끝 포인트 도달
                else:
                    answer.append(cnt)
    return min(answer) if answer else -1


N = 12
Weak = [1, 5, 6, 10]
Dist = [1, 2, 3, 4]
print(solution(N, Weak, Dist))
# TODO
