1. 입국심사
``` python
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
```

    이진 탐색 문제는 오랜만이지만, 이전에 풀었던 문제들이랑 비슷한 문제라 거부감은 없었다.
    다만 right과 각 심사관마다 주어진 mid 시간 동안 몇 명의 사람을 심사할 수 있는지가 관건이었다.

    🔑 Keypoint : 각 심사관마다 주어진 mid 시간 동안 몇 명의 사람을 심사할 수 있는지 체크하기