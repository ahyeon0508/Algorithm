"""
백준 1753 최단경로
https://www.acmicpc.net/problem/1753
"""

import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())

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

for i in range(1, V + 1):
    if result[i] != INF:
        print(result[i])
    else:
        print("INF")