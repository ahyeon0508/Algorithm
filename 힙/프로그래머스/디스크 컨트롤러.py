jobs = [[0, 3], [1, 9], [2, 6]]

def solution(jobs):
    answer = 0
    start = 0
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1]) # 소요시간 우선 정렬

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start: # 해당 작업의 요청시간이 start(현재까지 진행된 작업 시간)보다 작으면
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            # 해당 시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                start += 1

    return answer // length

print(solution(jobs))