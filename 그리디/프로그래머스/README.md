1. 체육복
``` python
def solution(n, lost, reserve):
    reserve_list = set(reserve) - set(lost)
    lost_list = set(lost) - set(reserve)

    for i in reserve_list:
        if i - 1 in lost_list:
            lost_list.remove(i - 1)
        elif i + 1 in lost_list:
            lost_list.remove(i + 1)

    return n - len(lost_list)
```

    몇 가지 테스트가 계속 실패가 떠서 너무 답답했다.
    다른 분이 하신 것을 참고해보니 비슷한 원리로 접근했지만
    조건을 더 생각했어야 하는 문제였다.
    
    📖 참고 : https://wooaoe.tistory.com/78
        
    🔑 Keypoint : 집합 - 집합, remove
    
2. 조이스틱
``` python
def solution(name):
    moves = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]

    pos = 0
    answer = 0

    while True:
        answer += moves[pos]
        moves[pos] = 0

        if sum(moves) == 0:
            break

        left = 1
        right = 1

        while moves[pos - left] == 0:
            left += 1

        while moves[pos + right] == 0:
            right += 1

        if left >= right:
            pos += right
            answer += right

        else:
            pos -= left
            answer += left

    return answer
```

    탐욕법의 굴레에 빠졌던 문제였다. 위치를 옮기는게 어려웠다ㅠㅠ
    
    📖 참고 : https://dev-note-97.tistory.com/96
        
    🔑 Keypoint : 위치 옮기기
    

3. 단속카메라
``` python
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾음

    for route in routes:
        if camera < route[0]: # 현재 카메라 위치로 해당 차량을 만나지 못했다는 의미
            answer += 1
            camera = route[1] # 가장 최근 카메라의 위치 갱신
    return answer
```

    문제 이해부터 힘들었던 문제이다ㅠㅠ
    이렇게 짧게 풀 수 있을지는 몰랐당..
    
    📖 참고 : https://wwlee94.github.io/category/algorithm/greedy/speed-enforcement-camera/
        
    🔑 Keypoint : routes를 차량이 나간 지점 (진출) 기준으로 정렬