1. 1이 될때까지
``` python
while n != 1:
    if n % k != 0:
        n -= 1
        count += 1
    else:
        n //= k
        count += 1
```

    전형적인 그리디 기법으로 풀면 풀린다!
            
    🔑 Keypoint : 그리디
    
1. 1이 될때까지(정답)
``` python
while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1 
    n //= k

result += (n - 1)
```

    시간 복잡도를 log로 푼 방법이다.
    이런 방법을 생각하시다니 나동빈님은 정말 대단하시다..
            
    🔑 Keypoint : 시간 복잡도 줄이기

2. 모험가 길드
``` python
for i in M:
    count += 1
    if count >= i:
        result += 1
        count = 0
```

    처음에 내림차순으로 풀었다가 다른 테스트 케이스에 걸려서 다시 오름차순으로 풀었다.
            
    🔑 Keypoint : 오름차순