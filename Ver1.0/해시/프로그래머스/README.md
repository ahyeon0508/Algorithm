1. 완주하지 못한 선수
``` python
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```

    풀다보니 이전에 비슷한 문제를 풀었던 것 같다는 생각이 들었다. 하지만 기억이 안 났다ㅎㅎ
    열심히 풀고 제출했는데 테스트 문제는 다 통과 but 효율성에서 계속 오류가..😯
    그래서 아래의 참고 사이트를 봤는데,, 예전의 기억들이 팍팦파가파팍났다ㅋㅋㅋㅋ
    이래서 복습은 필수인 것 같다..
    그리고 아직 hash 함수를 한 번도 공부해보지 않아 이번 문제는 무작정 풀어본 문제였는데
    얼른 hash 함수를 공부해서 써봐야겠다는 생각이 들었다!
    
    📖 참고 : https://ychae-leah.tistory.com/23 

    🔑 Keypoint : collections.Counter() 모듈 or hash()
    
2. 베스트앨범
``` python
def solution(genres, plays):
    answer = []
    albums_total = {}
    albums = {}

    for i in range(len(genres)):
        albums_total[genres[i]] = albums_total.get(genres[i], 0) + plays[i]
        albums[genres[i]] = albums.get(genres[i], []) + [(plays[i], i)]

    genreSort = sorted(albums_total.items(), key = lambda x: -x[1])

    for (genre, play) in genreSort:
        albums[genre] = sorted(albums[genre], key = lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in albums[genre][:2]]

    return answer
```

    효율성에 신경쓰다 보니 약간 당황했던 문제이다. (근데 채점할 때 보니 효율성은 테스트 안 했..)
    이 문제는 딕셔너리의 get()과 sort를 잘 사용하면 쉽게 풀 수 있는 문제인 것 같다.
    근데 이 문제 예전에 푼 기록이 있다.. 뭐지..?? 심지어 이번이랑 유사하게 풀었음ㅋㅋㅋㅋㅋㅋ
    
    📖 참고 : https://johnyejin.tistory.com/50

    🔑 Keypoint : 딕셔너리의 get() 사용
    
3. 전화번호 목록
``` python
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
```

    생각나는 대로 코드를 짜서 정확도와 효율성 테스트에 성공할지 몰랐는데 성공했다.
    다른 분들이 짠 코드를 보니 나와 비슷하게 푸신 분도 계시긴 했다🖐🖐
    sort함수와 zip함수로 푸신 분들과 계셨고 문제의 의도대로 해시로 푸신 분들도 계셨다.
    
    🔑 Keypoint : 문자열 인덱싱
    
4. 위장
``` python
def solution(clothes):
    dict_clothes = {}
    answer = 1
    for i in range(len(clothes)):
        dict_clothes[clothes[i][1]] = dict_clothes.get(clothes[i][1], 0) + 1

    for cloth in dict_clothes.keys():
        answer *= (dict_clothes[cloth] + 1)

    return answer - 1
```

    조합으로 개수를 계산하면 된다.
    대신 해당 카테고리의 아이템을 착용하지 않은 경우를 위해 모든 카테고리에 +1를 해줘야 한다.
    또한 어떤 아이템도 착용하지 않는 경우는 없으니 마지막에 -1을 해줘야 한다.
    Keypoint를 생각하지 못 해 아래의 사이트를 참고해서 아이디어를 얻고 내 힘으로 풀어봤다.
    풀고 나서 다른 분들의 코드를 보니 reduce와 counter 함수를 통해 간결하게 짤 수 있다는 것을 알았다.
    reduce 함수는 처음 봤당.. 파이썬 공부도 꾸준히 해야겠다는 생각을 했다(공부할 거 정말 많다👩‍💻)
    
    📖 참고 : https://itholic.github.io/kata-camouflage/
    
    🔑 Keypoint : 해당 카테고리의 아이템을 착용하지 않은 경우, 어떤 아이템도 착용하지 않는 경우