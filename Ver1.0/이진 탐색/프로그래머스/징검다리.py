distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2

import math

def solution(distance, rocks, n):
    answer = 0

    left = 1
    right = distance

    rocks.sort()
    while left <= right:
        mid = (left + right) // 2
        pre_rock = 0
        num_of_rock = 0
        m_min = math.inf
        for rock in rocks:
            if rock - pre_rock < mid:
                num_of_rock += 1
            else:
                m_min = min(m_min, rock - pre_rock)
                pre_rock = rock

        if num_of_rock > n:
            right = mid - 1
        else:
            answer = m_min
            left = mid + 1

    return answer

print(solution(distance, rocks, n))