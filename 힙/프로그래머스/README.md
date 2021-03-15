1. 더 맵게
``` python
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        first = heapq.heappop(scoville)

        if first >= K:
            break

        if len(scoville) <= 0:
            return -1

        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1

    return answer
```

    heapq 라이브러리를 몰라 deque로 풀었다가 시간초과에 걸렸다.
    시간 복잡도를 작게 하기 위해 O(NlogN)의 시간 복잡도를 갖는 힙 정렬을 사용해야한다.
        
    📖 참고 : https://gurumee92.tistory.com/163    
        
    🔑 Keypoint : heapq
    
2. 디스크 컨트롤러
``` python
def solution(jobs):
    answer = 0
    start = 0
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1]) # 소요시간 우선 정렬

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start: # 해당 작업의 요청시간이 start(현재까지 진행된 작업 시간)보다 작으면
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            # 해당 시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                start += 1

    return answer // length
```

    여러 가지 블로그를 참고해본 결과 heapq를 사용해서 푸신 분들도 계셨다.
    다만 이 문제는 heapq를 쓰는게 더 어려워 보였다.
        
    📖 참고 : https://johnyejin.tistory.com/132  
        
    🔑 Keypoint : 해당 작업의 요청시간이 현재까지 진행된 작업 시간보다 작을때