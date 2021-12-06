numbers = "17"

from itertools import permutations

def solution(numbers):
    answer = 0
    clean_combination= []
    for i in range(1, len(numbers) + 1):
        combination =  list(permutations(numbers, i))
        clean_combination += [int(''.join(i)) for i in combination]

    for i in set(clean_combination):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0 and i != 0:
                cnt += 1
            if cnt >= 3:
                break
        if cnt == 2:
            answer += 1

    return answer

print(solution(numbers))