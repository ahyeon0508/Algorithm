1. 11728 배열 합치기
``` python
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = A + B
result.sort()

print(*result)
```

    쉽게 풀었지만 문제의 의도는 분할정복이라고 한다. (merge sort 이용)

    🔑 Keypoint : list + list