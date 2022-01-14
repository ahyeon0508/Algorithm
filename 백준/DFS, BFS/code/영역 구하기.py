from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    queue = deque([(i, j)])
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append((ny, nx))
                cnt += 1
    return cnt

m, n, k = map(int, input().split())
graph = [[0]*(n) for i in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result))