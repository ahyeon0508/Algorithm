priorities = [2, 1, 3, 2]
location = 2

from collections import deque

def solution(priorities, location):
    answer = 0
    clean_priorities = []

    for i, p in enumerate(priorities):
        clean_priorities.append([p, i])

    q = deque(clean_priorities)

    while len(q):
        property = q.popleft()
        if q and max(q)[0] > property[0]:
            q.append(property)
        else:
            answer += 1
            if property[1] == location:
                break

    return answer

print(solution(priorities, location))