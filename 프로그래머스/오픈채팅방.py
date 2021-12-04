def solution(record):
    answer = []
    member = {}
    actions = []

    for msg in record:
        action = msg.split()[0]
        if action in ('Enter', 'Change'):
            member[msg.split()[1]] = msg.split()[2]
        actions.append((action, msg.split()[1]))

    for actionInfo in actions:
        if actionInfo[0] == 'Enter':
            answer.append(member[actionInfo[1]] + "님이 들어왔습니다.")
        elif actionInfo[0] == 'Leave':
            answer.append(member[actionInfo[1]] + "님이 나갔습니다.")

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))