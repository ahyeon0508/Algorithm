"""
백준 1260 DFS와 BFS
https://www.acmicpc.net/problem/1260
"""
from collections import deque

def dfs(graph, V, visited):
    # 현재 노드 방문 처리
    visited[V] = True
    print(V, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, N+1):
        if not visited[i] and graph[V][i] == 1:
            dfs(graph, i, visited)

def bfs(graph, V, visited):
    queue = deque([V])
    # 현재 노드를 방문 처리
    visited[V] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        V = queue.popleft()
        print(V, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in range(1, N+1):
            if not visited[i] and graph[V][i] == 1:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [False] * (N+1)
dfs(graph, V, visited)
print()
visited = [False] * (N+1)
bfs(graph, V, visited)