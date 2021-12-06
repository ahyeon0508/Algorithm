def solution(lottos, win_nums):
    temp_cnt = len(list(set(lottos) & set(win_nums)))
    temp_high_rank = 7 - (temp_cnt + lottos.count(0))
    temp_low_rank = 7 - temp_cnt

    if 6 <= temp_high_rank:
        temp_high_rank = 6

    if 6 <= temp_low_rank:
        temp_low_rank = 6

    answer = [temp_high_rank, temp_low_rank]

    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))