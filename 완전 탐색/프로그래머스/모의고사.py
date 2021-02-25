answers = [1, 2, 3, 4, 5]

def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    first_cnt = 0; second_cnt = 0; third_cnt = 0;

    for idx, answer in enumerate(answers):
        if answer == first[idx % len(first)]:
            first_cnt += 1
        if answer == second[idx % len(second)]:
            second_cnt += 1
        if answer == third[idx % len(third)]:
            third_cnt += 1

    cnt_list = [first_cnt, second_cnt, third_cnt]
    answer = []

    for idx, cnt in enumerate(cnt_list):
        if cnt == max(cnt_list):
            answer.append(idx + 1)

    return answer

print(solution(answers))