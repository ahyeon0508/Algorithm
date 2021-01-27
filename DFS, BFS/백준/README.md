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
    