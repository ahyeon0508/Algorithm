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