from collections import deque

def bfs(graph, i, visited):
    num = [0] * (n+1)
    queue = deque([i])
    visited[i] = True

    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if visited[i] == False:
                queue.append(i)
                num[i] = num[q] + 1
                visited[i] = True

    return sum(num)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []

for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    result.append(bfs(graph, i, visited))

print(result.index(min(result)) + 1)