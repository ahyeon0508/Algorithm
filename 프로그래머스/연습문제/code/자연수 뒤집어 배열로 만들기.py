def solution(n):
    n = str(n)
    answer = [int(n[i]) for i in range(len(n)-1, -1, -1)]
    return answer

n = 12345
print(solution(n))