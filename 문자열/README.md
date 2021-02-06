1. 1225 이상한 곱셈
``` python
A, B = map(str, input().split())
result = 0

for i in range(len(A)):
    for j in range(len(B)):
        result += int(A[i]) * int(B[j])

print(result)
```

    오랜만에 쉬운 문제를 풀어서 기분이 업업됐다🥰
    이런 문제들만 가득하길..

    🔑 Keypoint : 문자열 인덱싱

2. 1157 단어 공부
``` python
# 딕셔너리 생성
word_dict = {}
for i in range(len(word)):
    word_dict[word[i]] = 0

for i in word_dict.keys():
    for j in range(len(word)):
        if i == word[j]:
            word_dict[i] += 1

# 가장 많이 나오는 알파벳
for alphabet, num in word_dict.items():
    if num == max(word_dict.values()):
        cnt += 1
        result = alphabet

if cnt != 1:
    print("?")
else:
    print(result)
```

    이 문제도 쉽게 풀었다! 2차 행복😁
    먼저 모든 알파벳을 대문자로 바꾸고, 딕셔너리로 알파벳에 대한 개수를 저장해준다.
    그리고 가장 많이 나오는 알파벳을 찾으면 된다. 만약 가장 많이 나오는 알파벳이 2개 이상이면 ?을 출력할 수 있도록 한다.

    🔑 Keypoint : 딕셔너리 이용