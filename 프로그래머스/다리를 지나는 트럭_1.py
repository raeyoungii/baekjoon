from collections import deque


def solution(bridge_length, weight, truck_weights):
    over = deque()
    ing = deque()
    wait = deque(truck_weights)
    time = deque()
    cnt = 0
    while True:
        if len(over) == len(truck_weights):
            break
        if ing:
            if time[0] >= bridge_length:
                over.append(ing.popleft())
                time.popleft()
        if wait:
            if sum(ing) + wait[0] <= weight:
                ing.append(wait.popleft())
                time.append(0)
        for i in range(len(time)):
            time[i] += 1
        cnt += 1
    answer = cnt
    return answer


Bridge_length, Weight, Truck_weights = 2, 10, [7, 4, 5, 6]
Answer = solution(Bridge_length, Weight, Truck_weights)
print(Answer)
