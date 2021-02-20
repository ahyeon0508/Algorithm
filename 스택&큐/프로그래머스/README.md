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
    
    🔑 Keypoint : 스택