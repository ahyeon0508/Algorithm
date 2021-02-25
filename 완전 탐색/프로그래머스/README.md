1. 모의고사
``` python
def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    first_cnt = 0; second_cnt = 0; third_cnt = 0;

    for idx, answer in enumerate(answers):
        if answer == first[idx % len(first)]:
            first_cnt += 1
        if answer == second[idx % len(second)]:
            second_cnt += 1
        if answer == third[idx % len(third)]:
            third_cnt += 1

    cnt_list = [first_cnt, second_cnt, third_cnt]
    answer = []

    for idx, cnt in enumerate(cnt_list):
        if cnt == max(cnt_list):
            answer.append(idx + 1)

    return answer
```

    문제가 이해되지 않아 당황스러웠었당..
    학생들이 찍는 패턴을 %연산자를 이용해서 풀면 되는 문제이다.
    문제를 이해하니 쉽게 풀렸던 문제이다.
    
    📖 참고 : https://rain-bow.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC
    
    🔑 Keypoint : 학생들이 찍는 패턴 파악하기