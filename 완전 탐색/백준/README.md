1. 백준 10819 차이를 최대로
``` python
nPr = permutations(list(map(int, input().split())))
result = 0

for num in nPr:
    sum = 0
    for i in range(n-1):
        sum += abs(num[i]-num[i+1])
    result = max(result, sum)
```

    규칙을 찾으려다 실패한 문제이다😂
    순열을 뽑아서 주어진 식대로 더하는 작업을 반복하고 그 중 가장 큰 값을 출력하면 된다.

    🔑 Keypoint : 순열 사용
    