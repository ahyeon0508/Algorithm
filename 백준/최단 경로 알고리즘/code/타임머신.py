# 벨만 포드 알고리즘
def bf(start):
    dist[start] = 0
    for i in range(n):
        # 매 반복 마다 모든 간선 확인
        for j in range(m):
            cur = bus_routes_list[j][0]
            next = bus_routes_list[j][1]
            cost = bus_routes_list[j][2]
            if dist[cur] != INF and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                # 음수 순환 존재 파악
                if i == n-1:
                    return True
    return False

# 도시의 개수(노드), 버스 노선의 개수(간선) 입력
n, m = map(int, input().split())

# 버스 노선 정보
bus_routes_list = []
INF = int(1e9)
for _ in range(m):
    bus_routes_list.append(list(map(int, input().split())))

# 최단 거리 테이블
dist = [INF] * (n+1)

# 벨만 포드 알고리즘 수행
cycle = bf(1)

if cycle:
    print(-1)
else:
    for i in range(2, n+1):
        # 해당 도시로 가는 경로가 없을 경우
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])