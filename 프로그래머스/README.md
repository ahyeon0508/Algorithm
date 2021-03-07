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