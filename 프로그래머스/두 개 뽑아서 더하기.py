from itertools import combinations
def solution(numbers):
    answer = []
    temp = list(combinations(numbers, 2))
    for i in temp:
        answer.append(i[0] + i[1])
    answer = list(set(answer))
    answer.sort()
    return answer