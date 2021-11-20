1. 가운데 글자 가져오기
``` python
def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        answer += s[int(len(s) / 2 - 1):int(len(s) / 2 + 1)]
    else:
        answer += s[int(len(s) / 2)]
    return answer
```

    오랜만에 쉬운 문자열 문제!

    🔑 Keypoint : 문자열 인덱싱

2. 같은 숫자는 싫어
``` python
def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0 or answer[-1] != i:
            answer.append(i)
    return answer
```

    이 문제도 문자열 인덱싱만 잘하면 된다!

    🔑 Keypoint : 문자열 인덱싱

3. 없는 숫자 더하기
``` python
def solution(numbers):
    answer = 0
    number_list = [i for i in range(10)]
    for i in number_list:
        if i not in numbers:
            answer += i
    return answer
```

    쉽게 풀었지만 다른 사람들의 코드를 보고 정말 놀랬다.
    45-sum(numbers)를 해주면 더 간단하게 풀 수 있다는 것에..

    🔑 Keypoint : for문 or 수학