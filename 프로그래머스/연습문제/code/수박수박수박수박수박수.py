def solution(n):
    s = "수박"
    if n % 2 == 0:
        answer = s * (n // 2)
    else:
        answer = s * (n // 2) + '수'
    return answer

n = 3
print(solution(n))