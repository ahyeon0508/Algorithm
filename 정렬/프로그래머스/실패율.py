def solution(N, stages):
    fail = []
    length = len(stages)
    for i in range(1, N+1):
        temp_cnt = stages.count(i)

        if length == 0:
            fail.append((i, 0))
        else:
            fail.append((i, temp_cnt / length))

        length -= temp_cnt

    fail.sort(key = lambda x: -x[1])
    fail = [i[0] for i in fail]
    return fail

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))