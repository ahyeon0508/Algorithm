from collections import deque

dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 0, 1, -1, 0, 1, -1]

def bfs():
    while queue:
        i, j = queue.popleft()

        for x, y in zip(dx, dy):
            nx = i + x
            ny = j + y

            if nx < 0 or nx >= n or ny >= m or ny < 0:
                continue

            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[i][j] + 1

n, m = map(int, input().split())

graph = []
queue = deque()
for i in range(n):
    temp = list(map(int, input().split()))
    for t in range(m):
        if temp[t] == 1:
            queue.append((i, t))
    graph.append(temp)

bfs()
result = 0
for i in range(n):
    for j in range(m):
        result = max(result, graph[i][j])

print(result - 1)