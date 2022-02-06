from collections import deque

graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0

# 뿌요 터뜨리는 함수
def bfs(a, b, c):
    queue = deque() # 방문한 공간 확인
    queue.append((a, b))

    pang = deque() # 터뜨릴 수 있는 좌표 저장
    pang.append((a, b))

    visited = [[False] * 6 for _ in range(12)] # 방문한 공간 확인
    visited[a][b] = True
    count = 1
    flag = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > 11 or ny < 0 or ny > 5:
                continue
            if graph[nx][ny] == c and not visited[nx][ny]:
                queue.append((nx, ny))
                pang.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    # 터뜨리기
    if count >= 4:
        flag = 1
        for x, y in pang:
            graph[x][y] = "."

    return flag

# 맵 정리해주는 함수
def organize():
    for y in range(6):
        queue = deque()
        for x in range(11, -1, -1): # 아래로 떨어지는 형식이기에 11부터 0까지 돌기
            if graph[x][y] != '.':
                queue.append(graph[x][y])
        for x in range(11, -1, -1):
            if queue:
                graph[x][y] = queue.popleft()
            else:
                graph[x][y] = '.'

# 입력
for _ in range(12):
    graph.append(list(input()))

while True:
    chk = 0
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.': # 색상이면
                chk += bfs(i, j, graph[i][j])

    if chk == 0: # 더이상 터뜨릴게 없음
        print(result)
        break
    else:
        result += 1
    organize()