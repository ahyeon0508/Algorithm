"""
백준 11724 연결 요소의 개수
https://www.acmicpc.net/problem/11724
"""
from collections import deque

def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

result = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        result += 1

print(result)