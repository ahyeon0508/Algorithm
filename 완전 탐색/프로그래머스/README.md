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
    
2. 소수 찾기
``` python
def solution(numbers):
    answer = 0
    clean_combination= []
    for i in range(1, len(numbers) + 1):
        combination =  list(permutations(numbers, i))
        clean_combination += [int(''.join(i)) for i in combination]

    for i in set(clean_combination):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0 and i != 0:
                cnt += 1
            if cnt >= 3:
                break
        if cnt == 2:
            answer += 1

    return answer
```

    조합으로 풀려다가 뭐지?라고 생각이 되어서 참고 사이트를 보니 순열로 푸는게 나은 문제였다.
    다른 분들은 에라토스테네스의 체로 풀었는데.. 역시 대단한 분들이 많다는 걸 느꼈다.
    
    📖 참고 : https://dev-jinee.tistory.com/7
    
    🔑 Keypoint : 소수의 조건(1과 자기 자신의 수로밖에 안 나눠지는 수)
    
3. 카펫
``` python
def solution(brown, yellow):
    for a in range(1, yellow + 1):
        if yellow % a == 0:
            b = yellow // a
            if 2 * a + 2 * b + 4 == brown:
                return [b + 2, a + 2]
```

    약수로만 풀려고 했더니 테스트 케이스에서 몇 개 걸렸다.
    역시나 쉽게 풀리는게 이상했다..ㅎㅎ
    약수 + 둘레의 길이를 잘 생각해줘야지 풀 수 있는 문제이다.
        
    🔑 Keypoint : 약수 + 둘레의 길이 생각하기