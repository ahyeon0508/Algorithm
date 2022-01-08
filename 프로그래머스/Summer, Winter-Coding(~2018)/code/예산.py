def solution(d, budget):
    money = 0

    if sum(d) <= budget:
        return len(d)

    d.sort()

    answer = []
    for i in d:
        money += i
        if money > budget:
            break
        answer.append(i)
    return len(answer)

d = [1,3,2,5,4]
budget = 9
print(solution(d, budget))