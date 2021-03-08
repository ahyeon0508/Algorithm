n = 5
lost = [4, 2]
reserve = [1, 3, 5]

def solution(n, lost, reserve):
    reserve_list = set(reserve) - set(lost)
    lost_list = set(lost) - set(reserve)

    for i in reserve_list:
        if i - 1 in lost_list:
            lost_list.remove(i - 1)
        elif i + 1 in lost_list:
            lost_list.remove(i + 1)

    return n - len(lost_list)

print(solution(n, lost, reserve))