# 테스트 1, 2, 4, 5 실패

progresses = [93, 30, 55]
speeds = [1, 30, 5]

from collections import deque

def solution(progresses, speeds):
    answer = []

    queue = deque(progresses)
    queue_speed = deque(speeds)

    day_list = []

    while queue:
        temp_day = 0

        progress = queue.popleft()
        speed = queue_speed.popleft()

        while progress < 100:
            progress += speed
            temp_day += 1

        day_list.append(temp_day)

    queue_day = deque(day_list)

    while queue_day:
        day = queue_day.popleft()
        cnt = 1
        delete = []

        for i in queue_day:
            if i < day:
                cnt += 1
                delete.append(i)
            else:
                break

        for i in delete:
            queue_day.remove(i)

        answer.append(cnt)

    return answer

print(solution(progresses, speeds))