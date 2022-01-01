def solution(n, words):
    answer = []

    for i in range(1, len(words)):
        # 앞사람이 말한 단어의 마지막 문자로 시작하는 단어여야 함
        if words[i-1][-1] != words[i][0]:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break

        # 이전에 등장했던 단어 사용 X
        elif words[i] in words[:i]:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break

    if len(answer) == 0:
        answer = [0, 0]

    return answer

n = 5
words = ["sbo", "observe", "effect", "e", "observe", "recognize", "encourage", "e", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
print(solution(n, words))