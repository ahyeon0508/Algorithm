from itertools import combinations

def solution(nums):
    answer = 0
    c_list = list(combinations(nums, 3))

    for c in c_list:
        isPrime = True

        for i in range(2, sum(c)):
            if sum(c) % i == 0:
                isPrime = False

        if isPrime == True:
            answer += 1

    return answer

nums = [1,2,3,4]
print(solution(nums))