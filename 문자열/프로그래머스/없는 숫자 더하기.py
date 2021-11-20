def solution(numbers):
    answer = 0
    number_list = [i for i in range(10)]
    for i in number_list:
        if i not in numbers:
            answer += i
    return answer