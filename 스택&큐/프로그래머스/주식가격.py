prices = [1, 2, 3, 2, 3]

from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)

    while queue:
        price = queue.popleft()
        time = 0
        for i in queue:
            time += 1
            if price > i:
                break
        answer.append(time)

    return answer

print(solution(prices))