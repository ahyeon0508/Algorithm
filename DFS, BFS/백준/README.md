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