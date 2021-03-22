n = 6
times = [7, 10]

def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        count = 0

        for time in times:
            count += mid // time # 각 심사관마다 주어진 mid 시간 동안 몇 명의 사람을 심사할 수 있는지

            if count >= n:
                break

        if count >= n:
            answer = mid
            right = mid - 1

        elif count < n:
            left = mid + 1

    return answer

print(solution(n, times))