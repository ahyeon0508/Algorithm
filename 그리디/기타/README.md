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
    