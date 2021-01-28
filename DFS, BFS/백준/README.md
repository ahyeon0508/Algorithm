1. 백준 1260 DFS와 BFS
``` python
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
```

    생각없이 무방향으로 풀었다가 출력값이 이상해서 고민했던 문제ㅎㅎ..
    양방향이므로 인접행렬로 풀면 된다.

    🔑 Keypoint : 입력으로 주어지는 간선은 양방향이다.

2. 백준 11724 연결 요소의 개수
``` python
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
```

    그렇게 어렵지 않았던 문제이다. DFS, BFS 둘 중에 아무거나 풀어도 된다.

    🔑 Keypoint : DFS/BFS
    
3. 백준 11725 트리의 부모 찾기
``` python
def dfs(start, tree, parents):
    for i in tree[start]: # 연결된 노드 모두 탐색
        if parents[i] == 0: # 한 번도 방문한 적이 없을 때
            parents[i] = start # 부모노드 저장
            dfs(i, tree, parents)

# dfs 함수 호출
dfs(1, tree, parents)

for i in range(2, N + 1):
    print(parents[i])
```

    어떻게 풀어야 할지 감이 안 와서 블로그를 참고해서 풀었다.
    이 문제도 DFS, BFS 둘 중에 아무거나 풀어도 된다.

    📖 참고 : https://developmentdiary.tistory.com/435

    🔑 Keypoint : DFS/BFS

4. 백준 4963 섬의 개수
``` python
def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        for i in range(8): # 상하좌우 대각선까지 탐색
            x = v[0] + dx[i]
            y = v[1] + dy[i]
            if 0 <= x <= h-1 and 0 <= y <= w-1 and map_graph[x][y]:
                map_graph[x][y] = 0
                queue.append([x, y])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    map_graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if map_graph[i][j]:
                cnt += 1
                bfs([i, j])

    print(cnt)
```

    상하좌우 대각선까지 탐색하는 방법에 대해 생각하는 것이 가장 어려웠다.
    사실 그게 핵심 포인트이기도 하다.
    
    📖 참고 : https://home-body.tistory.com/185

    🔑 Keypoint : 상하좌우 대각선 탐색하는 방법 찾기

5. 백준 7576 토마토
``` python
def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and store[x][y] == 0:
                store[x][y] = store[a][b] + 1
                queue.append([x, y])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())
store = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if store[i][j] == 1:
            queue.append([i, j])

bfs()

result = 0
for i in range(N):
    for j in range(M):
        temp = store[i][j]
        if temp == 0:
            print(-1)
            exit()
        result = max(result, temp)

print(result - 1) # 처음 익은 토마토가 1이기 때문에
```

    섬의 개수 문제와 비슷한 문제이긴 하지만... 난이도가 많이 업그레이드 된 문제이다.
    당분간 토마토🍅를 먹고 싶지 않게 만든 문제였다ㅎㅎ

    1. 익은 토마토를 미리 큐에 다 넣는다.
    2. 큐안의 토마토를 앞에서부터 뽑아낸다.
    3. 뽑은 토마토의 상하좌우에 안 익은 토마토가 있으면 +1 해주고 다시 큐에 넣는다.
    (반복)
    4. 큐 while문이 모두 돈 뒤에 0이 있으면 -1, 그렇지 않으면 store의 최대값을 비교해준다.
    5. 처음 익은 토마토가 1이기 때문에 최종값에서 -1를 빼준다.

    🔑 Keypoint : BFS