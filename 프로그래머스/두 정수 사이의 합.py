a = 3; b = 5

def solution(a, b):
    answer = 0

    if a == b:
        answer = a

    else:
        if a < b:
            for i in range(a, b + 1):
                answer += i
        else:
            for i in range(b, a + 1):
                answer += i

    return answer

print(solution(a, b))