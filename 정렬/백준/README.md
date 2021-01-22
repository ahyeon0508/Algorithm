1. 백준 2751 수 정렬하기 2
``` python
data.sort()
```

    N의 범위가 1,000,000까지 가기 때문에 시간 복잡도가 중요한 문제이다.
    시간 복잡도가 O(nlogn)인 정렬 기법으로 풀어야 한다.
    파이썬의 기본 정렬 함수가 O(nlogn)으로 구성되어 있어서 파이썬의 정렬 함수를 사용했다.
    또한 data.sort()와 sorted(data)를 사용할 수 있는데, data.sort()는 data 자체를 정렬한다.
    반면에, sorted(data)는 data에 영향을 미치지 않는다. 즉 정렬된 값을 보고 싶으면 리턴을 받아야 한다.

    🔑 Keypoint : 시간 복잡도가 O(nlogn)인 정렬 기법 사용하기
    
2. 백준 10814 나이순 정렬
``` python
member.sort(key=lambda data: int(data[0]))
```

    같은 나이일 수도 있다는 조건 때문에 조금 어려웠던 문제이다.
    딕셔너리로 구현하려고 했지만 키값은 중복될 수가 없으므로 그에 대한 해법으로 lambda를 찾아 사용했다.

    🔑 Keypoint : 나이는 같을 수도 있다, lambda 사용하기
    