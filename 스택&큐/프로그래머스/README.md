1. 다리를 지나는 트럭
``` python
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length

    while len(bridge) != 0:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time
```

    쉬운 문제였는데 풀다가 갑자기 멘붕에 빠져서 아래의 블로그를 참고했다.
    리스트를 2개나 만들어서 풀려고 했더니 멘붕에 빠졌던 것 같다.
    생각하는 힘이 아직도 많이 부족한 것 같다ㅠㅠ
    
    📖 참고 : https://donis-note.medium.com/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%A4%EB%A6%AC%EB%A5%BC-%EC%A7%80%EB%82%98%EB%8A%94-%ED%8A%B8%EB%9F%AD-python-8d03d1ac2a45
    
    🔑 Keypoint : 큐
    
2. 주식가격
``` python
def solution(prices):
    answer = []
    queue = deque(prices)

    while queue:
        price = queue.popleft()
        time = 0
        for i in queue:
            time += 1
            if price > i:
                break
        answer.append(time)

    return answer
```

    문제 이해하려고 문제만 한 5번을 읽은 것 같다.
    그러다 감이 안 와서 또 다른 분들의 도움을 받았다.
    나는 왜 아이디어가 안 떠오를까😔
    
    📖 참고 : https://kangmin1012.tistory.com/25
    
    🔑 Keypoint : 큐
    
3. 기능개발_answer
``` python
def solution(progresses, speeds):
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0

        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        if cnt:
            answer.append(cnt)

    return answer
```

    열심히 풀었는데 테스트 1, 2, 4, 5번이 실패했다ㅠㅠ (기능개발.py)
    왜 실패했는지 도저히 모르겠어서 여러 가지 블로그를 찾아보다가 아래의 방법을 보고 이해했다.
    그래도 오랜만에 내 힘으로 테스트 정확도 60%를 넘어서 뿌듯했다ㅎㅎ
    
    📖 참고 : https://duwjdtn11.tistory.com/483
    
    🔑 Keypoint : 큐
    
4. 프린터
``` python
def solution(priorities, location):
    answer = 0
    clean_priorities = []

    for i, p in enumerate(priorities):
        clean_priorities.append([p, i])

    q = deque(clean_priorities)

    while len(q):
        property = q.popleft()
        if q and max(q)[0] > property[0]:
            q.append(property)
        else:
            answer += 1
            if property[1] == location:
                break

    return answer
```

    참고한 사이트랑 비슷하게 풀었는데 이번에도 테스트 몇 개가 계속 실패했다..ㅠㅠ
    테스트 몇 개가 계속 실패했다는 것은 너무 예제에만 맞게 풀려고 했다는 뜻이다.
    알고리즘을 잘 생각해서 풀어야겠다.
    
    📖 참고 : https://eda-ai-lab.tistory.com/461
    
    🔑 Keypoint : 큐