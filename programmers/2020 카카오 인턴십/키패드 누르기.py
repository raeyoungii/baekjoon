def solution(numbers, hand):
    lst = []
    l = 10
    r = 12
    for i in numbers:
        if i == 0:
            i = 11
        if i % 3 == 1:
            lst.append('L')
            l = i
        elif i % 3 == 0:
            lst.append('R')
            r = i
        else:
            l_d = abs(l - i) // 3 + abs(l - i) % 3
            r_d = abs(r - i) // 3 + abs(r - i) % 3
            if l_d < r_d:
                lst.append('L')
                l = i
            elif r_d < l_d:
                lst.append('R')
                r = i
            else:
                if hand == "left":
                    lst.append('L')
                    l = i
                else:
                    lst.append('R')
                    r = i
    answer = ''.join(lst)
    return answer


Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Hand = "right"
print(solution(Numbers, Hand))
