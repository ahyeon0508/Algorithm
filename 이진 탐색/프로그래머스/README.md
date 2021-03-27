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
    
2. 징검다리
``` python
def solution(distance, rocks, n):
    answer = 0

    left = 1
    right = distance

    rocks.sort()
    while left <= right:
        mid = (left + right) // 2
        pre_rock = 0
        num_of_rock = 0
        m_min = math.inf
        for rock in rocks:
            if rock - pre_rock < mid:
                num_of_rock += 1
            else:
                m_min = min(m_min, rock - pre_rock)
                pre_rock = rock

        if num_of_rock > n:
            right = mid - 1
        else:
            answer = m_min
            left = mid + 1

    return answer
```

    이진 탐색 문제는 기준을 무엇으로 삼을지 파악하는게 가장 어려운 것 같다.
    
    📖 참고 : https://jinomadstory.tistory.com/121

    🔑 Keypoint : 최소값 기준으로 빠진 돌의 개수를 카운트