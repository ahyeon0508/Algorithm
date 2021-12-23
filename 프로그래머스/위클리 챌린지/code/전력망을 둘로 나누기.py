from collections import deque

def bfs(start, visited, graph):
    queue = deque([start])
    cnt = 1
    visited[start] = True
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = True

    return cnt

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for start, end in wires:
        visited = [False] * (n+1)
        visited[end] = True
        result = bfs(start, visited, graph)
        if abs(result - (n - result)) < answer:
            answer = abs(result - (n - result))

    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))