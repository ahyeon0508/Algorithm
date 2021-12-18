from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, x, y):
    queue = deque([(x, y)])
    answer = 1
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                answer += 1

    return answer

t = int(input())
for i in range(t):
    cnt = 0
    n, m, k = map(int, input().split())
    graph = [[0]*(m) for _ in range(n)]
    for j in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                cnt += 1
                bfs(graph, x, y)

    print(cnt)