def solution(num):
    cnt = 0

    if num == 1:
        return 0

    for i in range(500):
        cnt += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1

        if num == 1:
            return cnt

    return -1

num = 626331
print(solution(num))