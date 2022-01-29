def solution(n):
    answer = 0
    n = str(n)
    for i in range(len(n)):
        answer += int(n[i])

    return answer

# def solution(n):
#     return sum([int(i) for i in str(n)])

n = 123
print(solution(n))