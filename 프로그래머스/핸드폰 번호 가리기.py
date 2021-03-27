phone_number = "01033334444"

def solution(phone_number):
    for i in range(len(phone_number) - 4):
        phone_number = phone_number.replace(phone_number[i], '*', 1)

    return phone_number

print(solution(phone_number))