1. 백준 2965 캥거루 세마리
``` python
# '틀렸습니다'를 7번이나 마주하게 한 코드
input("캥거루의 초기 위치를 입력하세요: ")
```

    괜한 친절로 인해 '틀렸습니다'를 7번이나 마주했다ㅎㅎ..ㅠㅠ
    첫 문제이다 보니 문제 해석에 많은 시간을 들였다. 코딩은 쉬운 문제이다.

    🔑Keypoint : 첫 번째, 두 번째 숫자의 차이와 두 번째, 세 번째 숫자의 차이 비교

2. 백준 17608 막대기
``` python
# 시간 초과 해결방법
import sys
input = sys.stdin.readline

# 핵심 알고리즘
standard = stick[cnt - 1]
result = 1
for i in range(1, cnt):
    if stick[cnt-i-1] > standard:
        result = result + 1
        standard = stick[cnt-i-1]

```

    말로만 듣던 파이썬 '시간 초과' 문제 발생..(구글링으로 해결)
    경우의 수만 잘 생각하면 바로 풀 수 있는 문제이다.

    🔑Keypoint : 가장 마지막에 들어온 값만 가지고 비교하면 안 됨(ex: 5 5 6 3 5 4 -> 3)