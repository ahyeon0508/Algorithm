scoville = [1, 2, 3, 9, 10, 12]
K = 7

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        first = heapq.heappop(scoville)

        if first >= K:
            break

        if len(scoville) <= 0:
            return -1

        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1

    return answer

print(solution(scoville, K))