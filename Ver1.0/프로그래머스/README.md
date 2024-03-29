1. 두 정수 사이의 합
``` python
def solution(a, b):
    answer = 0

    if a == b:
        answer = a

    else:
        if a < b:
            for i in range(a, b + 1):
                answer += i
        else:
            for i in range(b, a + 1):
                answer += i

    return answer
```

    LEVEL1 문제 중에서도 사람들이 가장 많이 푼 문제를 풀어봤다.
    단순히 if-else 문과 for문을 쓰면 되는 쉬운 문제이다.
        
    🔑 Keypoint : if-else 문과 for문
    
2. 서울에서 김서방 찾기
``` python
def solution(seoul):
    answer = ''

    for idx, name in enumerate(seoul):
        if name == 'Kim':
            answer += "김서방은 " + str(idx) + "에 있다"

    return answer
```

    enumerate를 통해 idx를 구하면서 풀어봤다.
    굳이 이렇게 풀지 않아도 된다.
    index함수로 바로 풀어도 된다.
    
    🔑 Keypoint : idx 찾기
    
3. 2016년
``` python
def solution(a, b):
    dayOfTheWeek = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0

    for i in range(a - 1):
        day += month[i]

    day += b

    return dayOfTheWeek[day % 7 - 1]
```

    for문 대신에 sum 함수를 이용해서 day를 계산하면 더 짧게 풀 수 있다
    sum(month[:a-1]) + b
        
    🔑 Keypoint : 나머지 연산자
    
4. 핸드폰 번호 가리기
``` python
def solution(phone_number):
    for i in range(len(phone_number) - 4):
        phone_number = phone_number.replace(phone_number[i], '*', 1)

    return phone_number
```

    for문과 replace 함수를 통해 풀어봤다.
    다른 분들은 폰넘버 전체 길이에서 4를 빼서 *을 만들어주고 폰넘버의 마지막 4자리를 리턴해서 푸셨다(감탄)
        
    🔑 Keypoint : 문자열 변환

5. 두 개 뽑아서 더하기
``` python
def solution(numbers):
    answer = []
    temp = list(combinations(numbers, 2))
    for i in temp:
        answer.append(i[0] + i[1])
    answer = list(set(answer))
    answer.sort()
    return answer
```

    보통 combinations 혹은 이중 for문으로 푸는 것 같다.
        
    🔑 Keypoint : combinations 사용

6. 크레인 인형뽑기 게임
``` python
def solution(board, moves):
    bucket = []
    answer = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0

                if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
                    bucket.pop(-1)
                    bucket.pop(-1)
                    answer += 1

                break

    return answer*2
```

    뻘짓 대작전,, 그리고 실패,, 너무 어렵게 풀려고 했던 것 같다..
        
    🔑 Keypoint : bucket[-1] == bucket[-2]

7. 내적
``` python
def solution(a, b):
    answer = 0
    for num in zip(a, b):
        answer += num[0] * num[1]
    return answer
```

    파이썬 zip() 을 이용하여 풀어보았다.
    채점 결과 테스트 케이스는 성공했는데 내부적인 오류가 발생했다고 한다.. 뭐지..?
    (파이썬으로 풀었다고 체크는 되어 있음..)
        
    🔑 Keypoint : zip()

7. 오픈채팅방
``` python
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
```

    이중 for문으로 풀다가 시간 초과가 걸린 문제ㅠㅠㅠㅠ
    이제 풀 수는 있지만 시간 복잡도가 문제인 것 같다..
        
    🔑 Keypoint : 시간 복잡도

8. 숫자 문자열과 영단어
``` python
def solution(s):
    answer = ''
    num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    temp = ''
    for i in list(s):
        if i.isdigit():
            answer += str(i)
        else:
            temp += i
        if temp in num_dict.keys():
            answer += str(num_dict[temp])
            temp = ''
    return int(answer)
```

    시간 초과가 걸릴까봐 조마조마 하면서 풀다 보니 푸는데 10분정도 걸린 문제이다.
    시간 복잡도를 생각하지 않고 풀었더니 바로 풀렸다.
    다른 분들은 replace()를 이용해 간단하게 풀었다.. 대단쓰..
        
    🔑 Keypoint : replace()