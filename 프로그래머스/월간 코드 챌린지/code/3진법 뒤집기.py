def solution(n):
    trans = ''
    while n != 0:
        trans += str(n % 3)
        n = n // 3
    answer = 0
    for i in range(len(trans)):
        answer += 3**(len(trans)-1-i)*int(trans[i])
    # print(int(trans, 3))
    return answer

n = 45
print(solution(n))