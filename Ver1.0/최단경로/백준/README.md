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
    
2. 1504 특정한 최단 경로
``` python
def Dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    result = [INF for _ in range(N + 1)]
    result[start] = 0
    while q:
        dis, s = heapq.heappop(q)
        if dis > result[s]:
            continue
        for d, x in G[s]:
            d += dis
            if d < result[x]:
                result[x] = d
                heapq.heappush(q, [d, x])
    return result

N, E = map(int, input().split())

G = [[] for _ in range(N + 1)]

for _ in range(E):
    start, end, distance = map(int, input().split())
    G[start].append([distance, end])
    G[end].append([distance, start])

D1, D2 = map(int, input().split())

dis1 = Dijkstra(1) # 1->D1 1->D2
dis2 = Dijkstra(D1) # D1->D2 D1->N
result1 = dis1[D1] + dis2[D2] + Dijkstra(D2)[N] # 1->D1->D2->N
result2 = dis1[D2] + dis2[D2] + dis2[N] # 1->D2->D1->N

if result2 >= INF and result1 >= INF:
    print(-1)
else:
    print(min(result1, result2))
```

    1753번 문제에서 조금 더 어려운 문제이다.
    시작 - a - b - 끝, 시작 - b - a - 끝
    위의 두 케이스에 대해 생각해보면 된다. (말만 쉽지..ㅎㅎ)
    
    📖 참고 : https://developmentdiary.tistory.com/392

    🔑 Keypoint : 다익스트라 알고리즘을 여러번 적용시킨다.