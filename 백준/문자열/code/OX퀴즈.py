n = int(input())
for i in range(n):
    answer = 0
    score = 0

    results = input()
    for result in results:
        if result == 'O':
            score += 1
            answer += score
        else:
            score = 0

    print(answer)