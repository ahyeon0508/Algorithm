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
    
4. 큰 수 만들기
``` python
def solution(number, k):
    stack = []

    for i, num in enumerate(number):
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        if k == 0:
            stack.append(number[i:])
            break

        stack.append(num)

    stack = stack[:-k] if k > 0 else stack
    answer = "".join(stack)
    return answer
```

    컴비네이션으로 풀면 안 될 것 같지만 그렇게 풀어보니 역시나 시간 초과 에러가 났다.
    결국 스택으로 풀면 되는 문제였다고 한다.
    
    📖 참고 : https://gurumee92.tistory.com/162
        
    🔑 Keypoint : 앞자리를 최고 큰 수로 만들기
    
5. 구명보트
``` python
def solution(people, limit):
    answer = 0
    i = 0
    j = len(people) - 1

    people.sort()

    while i <= j:
        answer += 1

        if people[i] + people[j] <= limit:
            i += 1

        j -= 1

    return answer
```

    나름 쉬웠던 문제!
    가장 가벼운 사람과 가장 무거운 사람의 무게를 더하는 것이 포인트이다.
        
    🔑 Keypoint : 가장 가벼운 사람과 가장 무거운 사람의 무게 더하기
    
6. 섬 연결하기
``` python
def solution(n, costs):
    ans = 0
    costs.sort(key = lambda x: x[2])
    routes = set([costs[0][0]])
    while len(routes)!=n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans
```

    크루스칼 알고리즘으로 푸는 문제이다.
    크루스칼 알고리즘인가?라는 생각은 떠올렸지만 크루스칼 알고리즘을 구현하는 법을 까먹어서..
        
    📖 참고 : https://jisun-rea.tistory.com/entry/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level3-%EC%84%AC-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0-%ED%83%90%EC%9A%95%EB%B2%95
    
    🔑 Keypoint : costs를 2번째 원소로 sort하기