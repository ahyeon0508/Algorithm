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