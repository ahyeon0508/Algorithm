"""
백준 1504 특정한 최단 경로
https://www.acmicpc.net/problem/1504
"""

import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

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