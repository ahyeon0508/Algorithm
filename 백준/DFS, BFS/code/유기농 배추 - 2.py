from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, i, j):
    queue = deque([(i, j)])
    graph[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*(N) for _ in range(M)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1
    
    print(cnt)