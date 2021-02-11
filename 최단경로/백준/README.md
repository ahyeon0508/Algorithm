1. 1753 최단경로
``` python
G = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end, distance = map(int, input().split())
    G[start].append([distance, end])

result = [INF for _ in range(V + 1)]
result[K] = 0 # 시작점은 0

# 데이터를 정렬된 상태로 저장하기 위해서 사용
q = []
heapq.heappush(q, [0, K]) # O(logN)

while q:
    dis, end = heapq.heappop(q)

    if result[end] < dis:
        continue

    for d, x in G[end]: # 연결된 노드 탐색
        d += dis
        if d < result[x]:
            result[x] = d
            heapq.heappush(q, [d, x])
```

    알고리즘 시간에 최단경로 문제를 배울때 다익스트라 알고리즘을 배웠던 기억이 난다.
    하지만 그 이후로 처음 보는거라 다 까먹어서 고생했다😔😔
    새로운 마음을 가지고 다시 공부했다😸
    
    📖 참고 : https://mattlee.tistory.com/50
             https://developmentdiary.tistory.com/391 

    🔑 Keypoint : 다익스트라 알고리즘