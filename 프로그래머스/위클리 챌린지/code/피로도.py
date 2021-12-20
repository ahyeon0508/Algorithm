from itertools import permutations

def solution(k, dungeons):
    per_list = list(permutations(dungeons, len(dungeons)))
    answer = []

    for per in per_list:
        temp_k = k
        cnt = 0
        for i in per:
            if temp_k >= i[0]:
                temp_k -= i[1]
                cnt += 1
        answer.append(cnt)

    return max(answer)

k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))