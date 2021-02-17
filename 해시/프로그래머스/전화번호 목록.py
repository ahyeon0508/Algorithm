phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    for phone in phone_book:
        phone_len = len(phone)
        for i in range(len(phone_book)):
            if phone == phone_book[i][0:phone_len] and phone_len < len(phone_book[i]):
                answer = False
                return answer

            else:
                answer = True

    return answer

print(solution(phone_book))