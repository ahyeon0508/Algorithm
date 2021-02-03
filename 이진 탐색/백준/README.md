1. 10815 숫자 카드
``` python
def binary_search(num_list, target):
    start = 0
    end = len(num_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] == target:
            return 1
        elif num_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0
```

    이진 탐색으로 풀어도 되고 set으로 풀어도 되는 문제이지만
    이진 탐색을 연습하고 있기 때문에 이진 탐색으로 풀어보았다.
    이진 탐색의 개념만 알고 있다면 간단하게 풀 수 있는 문제이다.

    🔑 Keypoint : 이진 탐색 / set

2. 10816 숫자 카드2
``` python
dicts = {}

for num in num_list:
    if num in dicts:
        dicts[num] += 1
    else:
        dicts[num] = 1

print(' '.join(str(dicts[target]) if target in dicts else '0' for target in check_list))
```

    이진 탐색으로 풀었는데 시간초과가 나서 당황한 문제이다😅
    이유는 이 문제는 target이 여러개 이고, 중복도 존재하기 때문이라고 한다.
    시간복잡도와 공간복잡도를 생각하는게 가장 어려운 것 같다😥

    📖 참고 : https://infinitt.tistory.com/288

    🔑 Keypoint : 딕셔너리 활용

3. 1654 랜선 자르기
``` python
def binary_search(length, N):
    start = 1
    end = max(length)
    while start <= end:
        mid = (start + end) // 2
        line = 0
        for i in length:
            line += i // mid

        if line >= N: # 랜선이 목표치 이상이면 길이를 늘리고 다시 line 개수 세기
            start = mid + 1
        else: # 랜선이 목표치 이하이면 길이를 줄이고 다시 line 개수 세기
            end = mid - 1
    print(end)
```

    문제는 이해됐지만 어떻게 접근해야할지 감이 안 와 아래의 사이트를 참고해서 풀었다.
    이 문제는 시간초과가 많이 나는 문제라고 한다.
    
    처음 알고리즘 문제를 풀었을 때보다 문제 이해력은 많이 향상됐지만 접근 방법에 대해 생각하는 힘💪이 아직 많이 부족한 것 같다. 꾸준히 풀 수 있도록 노력해야겠다.

    📖 참고 : https://claude-u.tistory.com/443

    🔑 Keypoint : 랜선의 길이를 움직여 랜선 개수를 채우는지 본다.

4. 2805 나무 자르기
``` python
def binary_search(height, M):
    start = 1
    end = max(height)
    while start <= end:
        mid = (start + end) // 2
        result = 0
        for i in height:
            if i >= mid:
                result += i - mid

        if result >= M:
            start = mid + 1
        else:
            end = mid - 1

    print(end)
```

    이진 탐색 문제이며 랜선 자르기와 유사한 문제이다.

    🔑 Keypoint : 나무의 높이를 움직여 미터를 맞춘다.

5. 2110 공유기 설치
``` python
def binary_search(data):
    start = 1
    end = data[-1] - data[0]
    result = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        cur = data[0]
        for i in range(1, N):
            if mid <= data[i] - cur:
                cnt += 1
                cur = data[i]

        # 더 많이 설치하려면 간격 줄이기
        if cnt >= C:
            result = mid
            start = mid + 1
        # 줄이려면 간격 늘리기
        else:
            end = mid - 1

    print(result)
```

    랜선 자르기와 나무 자르기랑 비슷한 문제인 것 같지만 조금 더 어려운 문제였다.
    집의 개수는 20만, 집의 좌표 범위는 10억이므로, 시간 복잡도(O(NlogX))는 20만*30=600만 정도이다.

    🔑 Keypoint : 공유기 수가 더 설치되어야 한다면 간격을 줄이고, 공유기 수를 줄여야 한다면 간격을 늘려야한다.