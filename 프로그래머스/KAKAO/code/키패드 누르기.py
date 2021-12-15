def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left = i
        elif i in [3, 6, 9]:
            answer += 'R'
            right = i
        else:
            if i == 0:
                i = 11

            absL = abs(i - left)
            absR = abs(i - right)

            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                right = i
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                left = i
            else:
                if hand.upper()[0] == 'L':
                    answer += 'L'
                    left = i
                else:
                    answer += 'R'
                    right = i

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))

