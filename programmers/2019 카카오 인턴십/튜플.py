from collections import Counter


def solution(s):
    # 숫자가 나타난 개수를 기준으로 내림차순으로 표현하면 답이 나옴 (중복되는 원소가 없기 떄문)
    answer = []
    for i in '{}':
        s = s.replace(i, '')  # 문자열에서 중괄호 제거
    # ,로 구분하고 Counter를 통해 각 숫자의 개수를 구하고 빈도 순서대로 for 문을 돌림
    for k, _ in Counter(map(int, s.split(','))).most_common():
        answer.append(k)  # answer 배열에 k 추가(k, _ 를 통해 숫자만 추가하고 개수는 표현하지 않음)
    return answer


S = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(S))
