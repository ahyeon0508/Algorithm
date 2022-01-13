# JadenCase 문자열 만들기

-------
### 🌞 문제
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
   
<b>제한사항</b>  
- s는 길이 1 이상인 문자열입니다.
- s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
- 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )

### 📝 입출력
|s|return|
|---|---|
|"3people unFollowed me"|"3people Unfollowed Me"|
|"for the last week"|"For The Last Week"|

### 👩‍💻 풀이
```python
def solution(s):
    s = s.split(" ")
    # print(s)
    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower()

    return ' '.join(s)
```

### 🔑 구현 아이디어
- 공백이라는 예외 케이스도 처리하기 위해 split을 할 때 split(" ")을 해준다.
- upper 함수와 lower 함수를 통해 첫 글자 영어는 대문자, 이외에는 소문자로 바꾼다.
  
### 🙋‍♀ 문제에 대한 나의 생각
- 공백을 생각하지 못 해서 풀지 못 한 문제였다. (이걸 어떻게 생각하지..)
- 어쩐지 레벨2치고 쉽더라🤦‍♀️
- split() vs split(" ")에 대해 자세히 알 수 있었던 문제였다.  
[참고](https://somjang.tistory.com/entry/Python-%EB%AC%B8%EC%9E%90%EC%97%B4-split-%EA%B3%BC-split-%EC%B0%A8%EC%9D%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0)

-------------
#### 📚 출처
- [JadenCase 문자열 만들기](https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3)
- [참고](https://bladejun.tistory.com/78)
#### 📅 공부 날짜 및 소요 시간
- ❌ 2022.01.14 (생각 및 구현 일부 성공 : 20분 -> 풀이 보고 이해 5분)  
#### ⭐ 개인적인 난이도 : 2 / 5