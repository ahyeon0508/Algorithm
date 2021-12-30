def solution(x, n):
    answer = [x * i for i in range(1, n+1)]
    return answer

x = 2
n = 5
print(solution(x, n))