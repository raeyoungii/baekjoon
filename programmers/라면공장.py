import heapq
from collections import deque


def solution(stock, dates, supplies, k):
    heap = []
    answer = 0
    dates = deque(dates)
    supplies = deque(supplies)
    while stock < k:
        while dates:
            if dates[0] <= stock:
                heapq.heappush(heap, -supplies.popleft())
                dates.popleft()
            else:
                break
        stock -= heapq.heappop(heap)
        answer += 1
    return answer


Stock = 4
Dates = [4, 10, 15]
Supplies = [20, 5, 10]
K = 30
ans = solution(Stock, Dates, Supplies, K)
print(ans)
