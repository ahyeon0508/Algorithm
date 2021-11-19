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