1. K번째수
``` python
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        if commands[i][0] <= commands[i][1]:
            select_array = sorted(array[commands[i][0] - 1: commands[i][1]])
            answer.append(select_array[commands[i][2] - 1])
        else:
            continue
    return answer
```

    문자열 인덱싱만 잘 하면 되는 문제였다!
    
    🔑 Keypoint : 문자열 인덱싱
    
2. 가장 큰 수
``` python
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    return str(int(''.join(numbers)))
```

    처음엔 순열로 풀었다가 시간 복잡도 때문에 테스트에 성공하지 못 했다ㅠㅠ
    문자열을 3번을 곱해줘서 해당 문자열을 3개 나열하고 정렬을 하면 된다.
    왜 3번인가에 대해 궁금증이 있었는데 각 number의 자릿수가 1000이하라는 조건이 있기 때문에 3번으로 설정했다.
    ex) numbers = [9, 991]일때 동일 문자열을 2번 나열하면 [99, 991991]이 된다. 이때 아직도 991이 99보다 더 크기 때문이다.
    그리고 string을 int로 변환하고 다시 string으로 변환하는 이유는 0일때가 문제이기 때문이다. ex) 0000
    
    📖 참고 : https://hocheon.tistory.com/48

    🔑 Keypoint : 동일한 문자열을 3번 나열
    
3. H-Index
``` python
def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        # h번 이상 인용된 논문이 h편 이상
        if citations[i] >= len(citations) - i:
            return len(citations) - i
    return 0
```

    스무스하게 푼줄 알았는데 제출 후에 있는 테스트에서 걸려버렸다.
    진짜 할말이 많은 문제이다. 처음엔 문제를 잘 이해한 줄 알았는데 아니었던 것 같다🤦‍♀️
    아직도 저 if문이 너무 신기하다ㅋㅋㅋㅋ 나중에 다시 풀어보면 못 풀수도..
    if문의 뜻은 h번 이상 인용된 논문이 h편 이상이라는 뜻이다인데 이걸 이해 못 해서 1시간을 넘게 썼다ㅠㅠ
    이 문제가 레벨2라는게 너무 안 믿긴다ㅎ.ㅎ
    
    🔑 Keypoint : h번 이상 인용된 논문이 h편 이상

4. 실패율
``` python
def solution(N, stages):
    fail = []
    length = len(stages)
    for i in range(1, N+1):
        temp_cnt = stages.count(i)

        if length == 0:
            fail.append((i, 0))
        else:
            fail.append((i, temp_cnt / length))

        length -= temp_cnt

    fail.sort(key = lambda x: -x[1])
    fail = [i[0] for i in fail]
    return fail
```

    역시 카카오 문제는 다르다..
    쉬울줄 알았는데 문제 해석부터 오래 걸림ㅠㅠㅠ
    내일 코테 화이팅..!!

    🔑 Keypoint : 문제 이해 잘하기