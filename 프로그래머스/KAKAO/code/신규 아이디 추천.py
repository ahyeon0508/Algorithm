def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()

    # 2단계
    for i in new_id:
        if i not in '~!@#$%^&*()=+[{]}:?,<>/':
            answer += i

    # 3단계
    for i in range(len(answer), 1, -1):
        if '.'*i in answer:
            answer = answer.replace('.'*i, '.')

    # 4단계
    if answer[0] == '.':
        answer = answer[1:]

    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]

    # 5단계
    if answer == '':
        answer = 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]

    if answer[-1] == '.':
        answer = answer[:-1]

    # 7단계
    if len(answer) <= 2:
        while True:
            answer += answer[-1]

            if len(answer) == 3:
                break

    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))